from setuptools import setup, find_packages

setup(
    name='CharTask',
    version='0.0.6',
    description='A package for creating tasks for characters.',
    author='James Evans',
    author_email='joesaysahoy@gmail.com',
    url='https://github.com/primal-coder/CharTask',
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.6',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Games/Entertainment :: Role-Playing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6'
    ],
    include_package_data=True,
    package_data={'CharTask': ['dicts/*.json']}
)