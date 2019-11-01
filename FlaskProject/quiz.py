from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABb-Ak-2e5jVqMjXiNl8NRk5_agpY8xWU95sbN3bDJiwA-V1s1RWmjXyab3ZwYoPO9l5M1ZQNrQ5TbWD0O44GRsiDW0p0xtGLLvUkbNJv2Tj9KGm1R-t8bCtyawnGroUSJatAip9LSVhgICKmwbZrwbg1EcWE80bfmd7wY4oQ3PC1rkh7bLHNq2I9lHSqdLx0lTGDVA'

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()