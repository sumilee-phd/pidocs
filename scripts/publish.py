# -*- coding: utf-8 -*-
"""piDocs 게시 — 허브(hub/)와 이 책(/ai-python/)을 _site/로 조립하고 gh-pages 가지로 올린다.

  python scripts/publish.py          # 조립만(_site/ 확인용)
  python scripts/publish.py --push   # 조립 후 gh-pages 푸시(공개 게시)
"""
import os
import shutil
import subprocess
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
SITE = os.path.join(ROOT, '_site')
DOMAIN = 'pidocs.aifusionlab.org'


def run(*cmd):
    print('>', ' '.join(cmd))
    subprocess.run(cmd, cwd=ROOT, check=True)


def main():
    run(sys.executable, os.path.join('scripts', 'make_site.py'))
    if os.path.exists(SITE):
        shutil.rmtree(SITE)
    run(sys.executable, '-m', 'mkdocs', 'build', '--strict', '-d', os.path.join('_site', 'ai-python'))
    for name in os.listdir(os.path.join(ROOT, 'hub')):
        shutil.copy2(os.path.join(ROOT, 'hub', name), os.path.join(SITE, name))
    print('조립 완료:', SITE)
    if '--push' in sys.argv:
        run('ghp-import', '-n', '-c', DOMAIN, '-b', 'gh-pages', '-m', 'piDocs 게시', '-p', '_site')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    os.environ.setdefault('NO_MKDOCS_2_WARNING', '1')
    main()
