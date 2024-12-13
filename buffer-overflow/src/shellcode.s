.global  _start
.section .text

_start:
        ldr x0,=shell
        mov x8,#221
        svc #0x0

.section .data
shell:
        .ascii "/bin/sh\0"
