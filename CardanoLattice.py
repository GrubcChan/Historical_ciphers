# Эта программа шифрует сообщение при помощи решетки Кардано

import numpy as np
import random


class CardanoLattice(object):
    def __init__(self, message):
        self.original_message = message
        self.message = message
        self.size = 2
        self.len_message = len(self.message)
        while pow(self.size, 2) < self.len_message:
            self.size += 2
        self.key = [[False] * self.size for i in range(self.size)]
        self.generate_key()

    def generate_key(self):
        check = []
        for turn in range(pow((self.size // 2), 2)):
            control = True
            position = random.randint(1, pow((self.size // 2), 2))
            while control:
                position = random.randint(1, pow((self.size // 2), 2))
                control = False
                for test in check:
                    if test == position:
                        control = True
            check.append(position)
            counter = 1
            for index_i in np.arange(0, self.size // 2, 1):
                for index_j in np.arange(0, self.size // 2, 1):
                    if counter == position:
                        self.key[index_i][index_j] = True
                    counter += 1
            self.rotation_key()

    # Поворот ключа
    def rotation_key(self):
        tmp = [[False] * self.size for i in range(self.size)]
        index_size = self.size - 1
        for index_i in np.arange(0, self.size, 1):
            for index_j in np.arange(0, self.size, 1):
                tmp[index_i][index_j] = self.key[index_size - index_j][index_i]
        self.key = tmp

    # Шифратор
    def encrypt(self):
        cipher = [[''] * self.size for i in range(self.size)]
        for index_i in np.arange(0, self.size, 1):
            for index_j in np.arange(0, self.size, 1):
                cipher[index_i][index_j] = chr(random.randint(33, 119))
        position = 0
        for turn in range(4):
            for index_i in np.arange(0, self.size, 1):
                for index_j in np.arange(0, self.size, 1):
                    if self.key[index_i][index_j]:
                        if position < self.len_message:
                            cipher[index_i][index_j] = self.message[position]
                        position += 1
            self.rotation_key()
        mas = ''
        for index_i in np.arange(0, self.size, 1):
            for index_j in np.arange(0, self.size, 1):
                mas += cipher[index_i][index_j]
        self.message = mas

    # Дешифратор
    def decoder(self):
        original_message = ''
        check_len = 0
        for turn in range(4):
            counter = 0
            for index_i in np.arange(0, self.size, 1):
                for index_j in np.arange(0, self.size, 1):
                    if self.key[index_i][index_j]:
                        if check_len < self.len_message:
                            original_message += self.message[counter]
                            check_len += 1
                    counter += 1
            self.rotation_key()
        self.message = original_message

    def analysis(self):
        key = []
        all_iteration = 0
        while key != self.key:
            key = [[False] * self.size for i in range(self.size)]
            check = []
            for turn in np.arange(0, pow((self.size // 2), 2), 1):
                control = True
                position = random.randint(1, pow((self.size // 2), 2))
                while control:
                    position = random.randint(1, pow((self.size // 2), 2))
                    control = False
                    for test in check:
                        if test == position:
                            control = True
                check.append(position)
                counter = 1
                for index_i in np.arange(0, self.size // 2, 1):
                    for index_j in np.arange(0, self.size // 2, 1):
                        if counter == position:
                            key[index_i][index_j] = True
                        counter += 1
                tmp = [[False] * self.size for i in range(self.size)]
                index_size = self.size - 1
                for index_i in np.arange(0, self.size, 1):
                    for index_j in np.arange(0, self.size, 1):
                        tmp[index_i][index_j] = key[index_size - index_j][index_i]
                key = tmp
                all_iteration += 1
        print(all_iteration)

#вар 6
