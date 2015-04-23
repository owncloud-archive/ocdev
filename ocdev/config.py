#!/usr/bin/env python3

import os
from configparser import ConfigParser


class UserSettings:

    def __init__(self, path):
        self.path = path
        self.config = ConfigParser()
        self.questions = {
            'setup': {
                'type': 'Please enter your preferred repo type (https|ssh)'
            },
            'startapp': {
                'author': 'Please enter your full name',
                'email': 'Please enter your email address',
                'homepage': 'Please enter your homepage'
            },
            'appstore': {
                'url': 'Please enter the appstore api url',
                'user': 'Please enter your appstore user',
                'password': 'Please enter your appstore password'
            },
            'devup': {
                'core': 'Please enter the preferred core branch to pull from'
            }
        }


    def read(self):
        if os.path.isfile(self.path):
            self.config.read(self.path)
        else:
            print('\nConfiguration not found! Empty configuration created: ' +
                  ' %s\n' % self.path)
            self.write({
                'setup': {
                    'type': 'https'
                },
                'startapp': {
                    'author': '',
                    'email': '',
                    'homepage': ''
                },
                'appstore': {
                    'url': 'https://api.owncloud.com/v1',
                    'user': '',
                    'password': ''
                },
                'devup': {
                    'core': 'master'
                }
            })


    def write(self, data):
        for section, values in data.items():
            if section not in self.config:
                self.config[section] = {}
            for key, value in values.items():
                self.config[section][key] = value
        with open(self.path, 'w') as f:
            self.config.write(f)


    def get_section(self, section):
        if not section in self.config:
            self.write({section: {}})
        return self.config[section]


    def get_value(self, section, value):
        if not section in self.config:
            self.write({section: {}})

        if value in self.config[section] and self.config[section][value].strip() != '':
            return self.config[section][value]
        else:
            answer = ''
            while answer.strip() == '':
                print(self.questions[section][value])
                answer = input('> ')
            print('')
            data = {}
            data[section] = {}
            data[section][value] = answer
            self.write(data)

            return answer

