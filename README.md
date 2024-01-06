# Hardware Encryption using DES and AES Modes in Verilog & OpenCV
I-CHIP Hackathon NITJ (1st Position) 

This project aims to design a hardware encryption and decryption scheme for the Data Encryption Standard (DES) algorithm in four different modes of operation: Electronic Code Book (ECB) mode, Cipher Block Chaining (CBC) mode, Cipher Feedback (CFB) mode, and Output Feedback (OFB) mode. 
The encryption and decryption process will be performed on a 1024x1024 grayscale image, where each pixel value ranges from 0 to 255. The hardware implementation will be synchronous with a base clock frequency of 100 MHz, and the output will be an encrypted image and the decrypted image obtained from it.

## Problem Statement
The task was to implement the following modes of operation for DES encryption and decryption:

Electronic Code Book (ECB) Mode: Each 64-bit block of the plaintext is encrypted independently using the DES algorithm.

Cipher Block Chaining (CBC) Mode: Each 64-bit block of the plaintext is XORed with the previous block's ciphertext before encryption using DES. The initialization vector (IV) is XORed with the first block of plaintext.

Cipher Feedback (CFB) Mode: The output of the previous encryption is XORed with the plaintext to produce the ciphertext. The feedback input to the DES algorithm is the previous block's ciphertext. The initialization vector (IV) is used as the first feedback input.

Output Feedback (OFB) Mode: The output of the previous encryption is XORed with the plaintext to produce the ciphertext. The feedback input to the DES algorithm is the previous block's ciphertext. The initialization vector (IV) is used as the first feedback input.

## Constraints

### Input
The input is a 1024x1024 grayscale image, where each pixel value is between 0 and 255.

![image](https://github.com/164adityakumar/Image_Encryption/assets/98655260/5101734b-d8b6-4984-936a-7603fb7b671f)

### Encryption and Decryption Scheme
The encryption and decryption schemes should be implemented in hardware using Verilog.

### Synchronous Operation
The hardware implementation should be synchronous with a base clock frequency of 100 MHz.

### Output
The output should be the encrypted image and the decrypted image obtained from it.
![image](https://github.com/164adityakumar/Image_Encryption/assets/98655260/9343bc6c-1396-4880-91cf-95908ac2279f)
