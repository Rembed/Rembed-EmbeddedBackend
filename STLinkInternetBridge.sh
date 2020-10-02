#~/bin/bash
while true
do
        cd /opt/st/stm32cubeide_1.4.0/plugins/com.st.stm32cube.ide.mcu.externaltools.stlink-gdb-server.linux64_1.4.0.202007081208/tools/bin
        ./ST-LINK_gdbserver -d -v -e -cp /opt/st/stm32cubeide_1.4.0/plugins/com.st.stm32cube.ide.mcu.externaltools.cubeprogrammer.linux64_1.4.0.202007081208/tools/bin
done
