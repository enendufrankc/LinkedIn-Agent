from setuptools import setup, find_packages

setup(
    version='0.1.0',
    author='Frank Enendu',
    author_email='frank@favai.onmicrosoft.com',
    description='LinkedIn Automation Tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/enendufrankc/linkedin-automation',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        'console_scripts': [
            'streamlit = streamlit.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
    license='MIT',
)