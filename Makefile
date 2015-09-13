assembler = nasm
disassembler = objdump -d

CDC.o: CDC.asm
  assembler -f elf CDC.asm -o CDC.o

CDC: CDC.o	
	ld CDC.o -o CDC
	disassembler CDC
	
install: CDC
	cp CDC /usr/bin
clean:
	rm *.o CDC
