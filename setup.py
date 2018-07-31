import setuptools
# import versioneer


if __name__ == "__main__":
    setuptools.setup(
        name='temporary',
        version="1.0",
        description='Example repo',
        author='Mojtaba Haghighatlari',
        author_email='mojtabah@buffalo.edu',
        url="https://github.com/mojtabah/temporary",
        license='BSD-3C',
        packages=setuptools.find_packages(),
        install_requires=[
        ],
        extras_require={
            'docs': [
                'sphinx',
                'sphinxcontrib-napoleon',
                'sphinx_rtd_theme',
                'numpydoc',
            ],
            'tests': [
                'pytest',
                'pytest-cov',
                'pytest-pep8',
                'tox',
            ],
        },

        tests_require=[
            'pytest',
            'pytest-cov',
            'pytest-pep8',
            'tox',
        ],

        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
            'Programming Language :: Python :: 3',
        ],
        zip_safe=False,
    )