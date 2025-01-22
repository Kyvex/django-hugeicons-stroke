from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='django_hugeicons_stroke',
    version='1.0.8',
    description='A Django templatetag library for using hugeicons free stroke icons',
	long_description=long_description,
	long_description_content_type='text/markdown',
    url='',
    author='Kyvex',
    author_email='developer.gdean@proton.me',
    license='GPL',
    packages=find_packages(include=['django_hugeicons_stroke', 'django_hugeicons_stroke.*']),  # ✅ Includes all submodules
    zip_safe=False,
    package_data={
        'django_hugeicons_stroke': ['templatetags/*.py'],  # ✅ Ensures templatetags is included
    },
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=['Django>=3.0'],
    python_requires='>=3.6',
)
