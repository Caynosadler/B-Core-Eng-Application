from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='
message = b'gAAAAABb68cVgFJy-yLLOEWoayDnEYvXUsqVbAi0t0Zk8P12EPppHPX71PE23a8v_ZyV7dbKEI6T7iwZRuPyCfbALT_mzhmGBdRLW3VfU-C3oVGN8s8w7S_x9wKdSmuEeYRCP6f4z4VMtR_SHviBes5lmID9BZVYlHlMNJbIhrvFgDsIK2StyV-16fYK1LdAv6S6JA7JQTlJ'

def main():
    f = Fernet(key)
    print(f.decrypt(message))

if __name__ == "__main__":
    main()
