#!/usr/bin/env python3
"""Inventory documentation candidates; never infer semantic review or agent access."""
import argparse
import datetime
import fnmatch
import hashlib
import json
import os
import stat
from pathlib import Path

TEXT = {'.md', '.mdx', '.markdown', '.rst', '.txt', '.adoc', '.asciidoc',
        '.org', '.html', '.htm', '.tex', '.mmd', '.mermaid'}
STRUCTURED = {'.yaml', '.yml', '.json', '.xml'}
EXTRACTION = {'.pdf', '.docx', '.doc', '.odt', '.rtf', '.pptx', '.ppt',
              '.xlsx', '.xls', '.ods', '.odp', '.pages', '.key', '.numbers'}
NAMES = {'readme', 'license', 'licence', 'changelog', 'changes', 'authors',
         'contributing', 'architecture', 'agents', 'claude', 'gemini',
         'instructions', 'security', 'notice', 'copying'}
PRUNED = {'.git', '.hg', '.svn', 'node_modules', '.venv', 'venv',
          '__pycache__', '.next', '.nuxt', 'dist', 'build', 'coverage'}


def matches(path, patterns):
    # Glob syntax follows fnmatch: '*' can span '/' in relative paths.
    return any(fnmatch.fnmatchcase(path, pattern) for pattern in patterns)


def inventory(root, includes=(), excludes=(), default_excludes=True):
    root = Path(root).resolve(strict=True)
    if not root.is_dir():
        raise ValueError('Project root must be a directory')
    docs, boundaries, errors = [], [], []
    scanned_files = 0

    def onerror(error):
        errors.append({'path': str(error.filename), 'error': str(error)})

    for base, dirs, files in os.walk(root, followlinks=False, onerror=onerror):
        dirs.sort()
        for name in dirs[:]:
            path = Path(base) / name
            rel = path.relative_to(root).as_posix()
            reason = ('symlink-directory' if path.is_symlink() else
                      'user-excluded-directory' if matches(rel, excludes) else
                      'default-pruned-directory' if default_excludes and name in PRUNED else None)
            if reason:
                dirs.remove(name)
                boundaries.append({'path': rel, 'reason': reason, 'contents_enumerated': False})
        for name in sorted(files):
            path = Path(base) / name
            rel = path.relative_to(root).as_posix()
            scanned_files += 1
            suffix = path.suffix.lower()
            kind = ('text' if suffix in TEXT or name.lower() in NAMES else
                    'structured-candidate' if suffix in STRUCTURED else
                    'requires-extraction' if suffix in EXTRACTION else
                    'explicit-candidate' if matches(rel, includes) else None)
            if path.is_symlink():
                boundaries.append({'path': rel, 'reason': 'symlink-file', 'contents_enumerated': False})
                continue
            if kind is None:
                continue
            entry = {'path': rel, 'kind': kind, 'review_state': 'pending'}
            if matches(rel, excludes):
                entry.update(review_state='excluded', reason='user-excluded-file')
                docs.append(entry)
                continue
            try:
                before = path.stat()
                if not stat.S_ISREG(before.st_mode):
                    entry.update(review_state='blocked', reason='not-regular-file')
                    docs.append(entry)
                    continue
                digest = hashlib.sha256()
                with path.open('rb') as stream:
                    for chunk in iter(lambda: stream.read(1024 * 1024), b''):
                        digest.update(chunk)
                after = path.stat()
                entry.update(bytes=after.st_size, sha256=digest.hexdigest())
                if (before.st_size, before.st_mtime_ns, before.st_ino) != (after.st_size, after.st_mtime_ns, after.st_ino):
                    entry.update(review_state='blocked', reason='changed-during-inventory')
            except OSError as error:
                entry.update(review_state='blocked', reason=str(error))
            docs.append(entry)
    docs.sort(key=lambda item: item['path'])
    boundaries.sort(key=lambda item: item['path'])
    return {
        'schema_version': 1,
        'root': str(root),
        'snapshot_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'scope': {'include_globs': list(includes), 'exclude_globs': list(excludes),
                  'default_pruned_names': sorted(PRUNED) if default_excludes else [],
                  'gitignore_applied': False, 'symlinks_followed': False},
        'counts': {'files_encountered': scanned_files, 'document_candidates': len(docs),
                   'pending': sum(item['review_state'] == 'pending' for item in docs),
                   'blocked': sum(item['review_state'] == 'blocked' for item in docs),
                   'excluded': sum(item['review_state'] == 'excluded' for item in docs)},
        'documents': docs, 'boundaries': boundaries, 'traversal_errors': errors,
        'notice': 'Discovery only; no semantic review or access measurement. Inspect unconventional documentation formats manually.'
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root')
    parser.add_argument('--include', action='append', default=[], help='Additional relative glob; does not override exclusions')
    parser.add_argument('--exclude', action='append', default=[], help='Exclude matching relative files/directories')
    parser.add_argument('--no-default-excludes', action='store_true')
    args = parser.parse_args()
    try:
        result = inventory(args.root, args.include, args.exclude, not args.no_default_excludes)
    except (OSError, ValueError) as error:
        parser.exit(2, str(error) + '\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
