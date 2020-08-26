from distutils.core import setup

setup(
    name='django-auditlog',
    version='0.7.1',
    packages=['auditlog', 'auditlog.migrations', 'auditlog.management', 'auditlog.management.commands'],
    package_dir={'': 'src'},
    url='https://github.com/jjkester/django-auditlog',
    license='MIT',
    author='Jan-Jelle Kester',
    description='Audit log app for Django',
    install_requires=[
        'python-dateutil>=2.8,<=3.0'
    ],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],        
)
