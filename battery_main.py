import serial

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

PORT = 'COM3'
#PORT = '/dev/ttyp5'

def main():
    logger = modbus_tk.utils.create_logger('console')

    try:
        #Connect to the slave
        master = modbus_rtu.RtuMaster(
            serial.Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0)
        )
        master.set_timeout(5.0)
        master.set_verbose(True)
        logger.info(f'Подключено к {PORT}')

        # logger.info(master.execute(3, cst.READ_HOLDING_REGISTERS, 0, 25))

        #send some queries
        # logger.info(master.execute(3, cst.READ_COILS, 0, 25))
        # logger.info(master.execute(3, cst.READ_DISCRETE_INPUTS, 0, 25))

        logger.info(master.execute(3, cst.READ_INPUT_REGISTERS, 0, 25))
        # master.execute(3, cst.READ_INPUT_REGISTERS, 0, 25)

        #logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 100, 12))
        #logger.info(master.execute(1, cst.WRITE_SINGLE_COIL, 7, output_value=1))
        #logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 100, output_value=54))
        #logger.info(master.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[1, 1, 0, 1, 1, 0, 1, 1]))
        #logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 100, output_value=xrange(12)))

    except modbus_tk.modbus.ModbusError as exc:
        # logger.error('%s- Code=%d', exc, exc.get_exception_code())
        logger.error(f'{exc} - Code = {exc.get_exception_code()}')

if __name__ == '__main__':
    main()
