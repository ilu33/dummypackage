from codecs import open as codecs_open
from setuptools import setup, find_packages


setup(name='dummypackage',
      version='0.0.2',
      description=u"Skeleton of a Python package",
      long_description="Dummy package",
      classifiers=[],
      keywords='',
      author=u"Iñaki Malerba",
      author_email='inaki@malerba.space',
      url='https://salsa.debian.org/salsa-ci-team/dummypackage',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'test': ['pexpect', 'pytest'],
      },
      entry_points="""
      [console_scripts]
      dummypackage=dummypackage.scripts.cli:cli
      """
)
