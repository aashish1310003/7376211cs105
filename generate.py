import random

class Generate:

    def __init__(self):
        self.pre_window = []
        self.current_window = []


    def check_prime(self, num):
            if num <= 1:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0 :
                    return False
            return True

    def is_prime(self):
        prime_numbers = []
        num = 2
        while len(prime_numbers) < 10:
            if self.check_prime(num):
                prime_numbers.append(num)
            num += 1
        self.current_window = prime_numbers
        if len(self.current_window) != len(self.pre_window):
            self.pre_window.extend(self.current_window)
        return prime_numbers

    def is_even(self):
        even_numbers = []
        num = 1
        while len(even_numbers) < 10:
            if num % 2 == 0 :
                even_numbers.append(num)
            num += 1
        self.current_window = even_numbers
        if len(self.current_window) != len(self.pre_window):
                self.pre_window.extend(self.current_window)
        return even_numbers


    def is_fibo(self):
        fibonacci_sequence = [0, 1]
        while len(fibonacci_sequence) < 10:
            next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]

            fibonacci_sequence.append(next_number)
        self.current_window = fibonacci_sequence
        if len(self.current_window)!= len(self.pre_window):
                self.pre_window.extend(self.current_window)
        return fibonacci_sequence


    def is_random(self):

        random_numbers = []
        num = random.randint(0, 1000)
        while len(random_numbers) < 10:
            if num not in random_numbers:
                random_numbers.append(num)
            num = random.randint(0, 1000)
        self.current_window = random_numbers
        if len(self.current_window) != len(self.pre_window):
                self.pre_window.extend(self.current_window)
        return random_numbers



