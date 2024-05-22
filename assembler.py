import plyplus

opcodeMap = {
    'add':  '0110011',
    'sub':  '0110011',
    'xor':  '0110011',
    'addi': '0010011',
    'xori': '0010011',
    'lw':   '0000011',
    'lh':   '0000011',
    'lb':   '0000011',
}

funct3Map = {
    'add':  '000',
    'sub':  '000',
    'xor':  '100',
    'addi': '000',
    'xori': '100',
    'lw':   '010',
    'lh':   '001',
    'lb':   '000',
}

funct7Map = {
    'add':  '0000000',
    'sub':  '0100000',
    'xor':  '0000000',
}

# Mapa de registros
registerMap = {
    'x0': '00000', 
    'zero': '00000', 
    'x1': '00001', 
    'x2': '00010', 
    'x3': '00011', 
    'x4': '00100', 
    'x5': '00101', 
    'x6': '00110', 
    'x7': '00111', 
    'x8': '01000', 
    'x9': '01001', 
    'x10': '01010', 
    'x11': '01011', 
    'x12': '01100', 
    'x13': '01101', 
    'x14': '01110', 
    'x15': '01111', 
    'x16': '10000', 
    'x17': '10001', 
    'x18': '10010', 
    'x19': '10011', 
    'x20': '10100', 
    'x21': '10101', 
    'x22': '10110', 
    'x23': '10111', 
    'x24': '11000', 
    'x25': '11001', 
    'x26': '11010', 
    'x27': '11011', 
    'x28': '11100', 
    'x29': '11101', 
    'x30': '11110', 
    'x31': '11111'
}

def toBinary(val,bits):
  # convierte un entero a su representación binario con un número fijo de bits.
  return format(val & ((1<<bits)-1),'0{}b'.format(bits))

def assembleInstruction(instruction):
    parts = instruction.split()
    mnemonic = parts[0]

    if mnemonic in funct7Map: #R-type instruction
        rd= registerMap[parts[1].strip(',')]
        rs1= registerMap[parts[2].strip(',')]
        rs2= registerMap[parts[3].strip(',')]
        funct3 = funct3Map[mnemonic]
        funct7= funct7Map[mnemonic]
        opcode = opcodeMap[mnemonic]
        binaryInstruction = funct7 + rs2 + rs1 + funct3 + rd + opcode

    elif mnemonic in funct3Map: # I-type instruction
        rd= registerMap[parts[1].strip(',')]
        rs1= registerMap[parts[2].strip(',')]
        imm= toBinary(int(parts[3]),12)
        funct3 = funct3Map[mnemonic]
        opcode = opcodeMap[mnemonic]
        binaryInstruction = imm + rs1 + funct3 + rd + opcode
    
    elif mnemonic in opcodeMap: # carga instrucciones
        rd= registerMap[parts[1].strip(',')]
        offsetParts= parts[2].strip(')').split('(')
        imm= toBinary(int(offsetParts[0]),12)
        funct3 = funct3Map[mnemonic]
        opcode = opcodeMap[mnemonic]
        binaryInstruction = imm + rs1 + funct3 + rd + opcode
    
    else:
       raise ValueError("instrucción desconocida: " + mnemonic)

    return binaryInstruction

# carga de la gramática
with open("riscv.g") as grm:
  parser = plyplus.Grammar(grm)
  parsedCode = parser.parse('''
               add x0, x0, x0
               add x0, x0, x0
               addi x0, x0, +100
               lw x0, 100(x0)
               lb x0, 0(x0)
               ''')
print(parsedCode)

#procesar cada instruccion
for instruction in parsedCode:
  binary = assembleInstruction(instruction.text)
  print(f'{instruction.text}-> {binary}')
