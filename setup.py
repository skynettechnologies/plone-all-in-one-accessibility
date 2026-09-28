# -*- coding: utf-8 -*-
"""Installer for the plone.all_in_one_accessibility package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.md', encoding='utf-8').read(),
])

setup(
    name='plone.all_in_one_accessibility',
    version='2.1.0',
    description="Website accessibility widget for improving WCAG 2.0, 2.1, 2.2 and ADA compliance!",
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone CMS',
    author='Skynet Technologies USA LLC',
    author_email='developer3@skynettechnologies.com',
    # project_urls={
    # },
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['plone'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.9",
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'z3c.jbot',
        'plone.api',
        'plone.app.dexterity',
        'plone.autoform',
    ],
    extras_require={
        # Only needed for the optional @widget REST endpoint under
        # api/services/widget/get.py; configure.zcml only loads that
        # package when plone.restapi is present, so it is intentionally
        # NOT in install_requires -- see configure.zcml.
        'restapi': [
            'plone.restapi',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = plone.all_in_one_accessibility.locales.update:update_locale
    """,
)
