assembler = nasm
disassembler = objdump -d

CDC.o: CDC.asm
  as -o CDC.o CDC.asm 
CDC: CDC.o	
	ld CDC.o -o CDC
	objdump -d CDC
	
install: CDC
	cp CDC /usr/bin
clean:
	rm *.o CDC
