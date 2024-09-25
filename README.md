# Python x8086 Assembler

## Overview

This project is a Python-based assembler for the x8086 architecture. It processes basic arithmetic and logical instructions such as ADD, SUB, AND, OR, XOR, TEST, CMP, and MOV. The assembler can manipulate the primary registers EAX, EBX, ECX, and EDX, along with their sub-registers. It updates and displays the CPU's status flags: Zero Flag, Sign Flag, Carry Flag, Overflow Flag, and Parity Flag. The assembler reads numbers in binary, decimal, and hexadecimal formats and is free-form, meaning the arrangement of characters does not affect execution.

## Features

- Supports the following instructions:
  - `ADD`, `SUB`, `AND`, `OR`, `XOR`, `TEST`, `CMP`, `MOV`
  
- Handles registers:
  - `EAX`, `EBX`, `ECX`, `EDX` and their sub-registers (AX, AL, AH, BX, BL, BH, CX, CL, CH, DX, DL, DH)

- Updates and displays the following flags:
  - Zero Flag (ZF)
  - Sign Flag (SF)
  - Carry Flag (CF)
  - Overflow Flag (OF)
  - Parity Flag (PF)

- Reads numbers in:
  - Binary (e.g., `0b1010`)
  - Decimal (e.g., `10`)
  - Hexadecimal (e.g., `0xA`)

- Free-form syntax: spacing, tabs, and newlines are ignored.
- Case insensitive: instructions and registers can be in any case.

## Requirements

- Python 3.x
- Basic understanding of x8086 assembly language.
