start: program;

program: inst+;

inst: 
    instr  regname ',' regname ',' regname // R instruction
  | insti  regname ',' regname ',' IMM     // I instruction
  | instil regname ',' offset;

offset: IMM '\(' regname '\)';

instname: instr | insti;

instr: 'add' | 'sub' | 'xor';
insti: 'addi' | 'xori';
instil: 'lw' | 'lh' | 'lb';

IMM: '[0]|(\-|\+)?[1-9][0-9]*';


regname: 
   'x0' | 'zero'
  | 'x1' | 'x2' | 'x3' | 'x4' | 'x5' | 'x6'| 'x7' | 'x8' | 'x9' | 'x10'
  | 'x11' | 'x12' | 'x13' | 'x14' | 'x15' | 'x16'| 'x17' | 'x18' | 'x19' | 'x20'
  | 'x21' | 'x22' | 'x23' | 'x24' | 'x25' | 'x26'| 'x27' | 'x28' | 'x29' | 'x30'
  | 'x31'
;

WS: '[ \t\r\n]+' (%ignore);