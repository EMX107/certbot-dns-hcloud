from setuptools import setup

install_requires = [
    'hcloud>=2.11.0',
    'certbot>=5.1.0',
    'setuptools'
]

setup(
    name='certbot-dns-hcloud',
    version='1.0.0',
    install_requires=install_requires,
    entry_points={
        "certbot.plugins": [
            "dns-hcloud = certbot_dns_hcloud._internal.dns_hcloud:Authenticator"
        ]
    },
)