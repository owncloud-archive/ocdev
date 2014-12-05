#!/usr/bin/env python3

import os
from configparser import ConfigParser


class UserSettings:

    def __init__(self, path):
        self.path = path
        self.config = ConfigParser()
        self.questions = {
            'startapp': {
                'author': 'Please enter your full name',
                'email': 'Please enter your email address',
                'homepage': 'Please enter your homepage'
            },
            'appstore': {
                'url': 'Please enter the appstore api url',
                'user': 'Please enter your appstore user',
                'password': 'Please enter your appstore password'
            }
        }


    def read(self):
        if os.path.isfile(self.path):
            self.config.read(self.path)
        else:
            print('\nConfiguration not found! Empty configuration created: ' +
                  ' %s\n' % self.path)
            self.write({
                'startapp': {
                    'author': '',
                    'email': '',
                    'homepage': ''
                },
                'appstore': {
                    'url': 'https://api.owncloud.com/v1',
                    'user': '',
                    'password': ''
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


    def get_value(self, section, value):
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

