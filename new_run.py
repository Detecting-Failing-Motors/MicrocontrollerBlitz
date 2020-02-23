import sys
import time
import numpy as np
import itertools
from ADS1256_definitions import *
from pipyadc import ADS1256
# In this example, we pretend myconfig_2 was a different configuration file
# named "myconfig_2.py" for a second ADS1256 chip connected to the SPI bus.
import ADS1256_default_config as myconfig_2

SHORT_CIRCUIT = POS_AIN0|NEG_AIN0
EXT2 = POS_AIN2|NEG_AINCOM

CH_OFFSET = np.array((0, 0), dtype=np.int)
GAIN_CAL  = np.array((1.0, 1.0), dtype=np.float)

CH_SEQUENCE = (EXT2, SHORT_CIRCUIT)

#begin
ads2 = ADS1256(myconfig_2)
ads2.drate = DRATE_30000
ads2.cal_self()

chip_ID = ads2.chip_ID
    print("\nADC No. 2 reported a numeric ID value of: {}.".format(chip_ID))
    # When the value is not correct, user code should exit here.
    if chip_ID != 3:
        print("\nRead incorrect chip ID for ADS1256. Is the hardware connected?")
		
		
CH_GAIN = ads2.v_per_digit * GAIN_CAL

time_read = 1
data_array = np.empty([1, 30000], dtype=int)

start = time.time()
    while (time.time() - start) <= time_read:
		value = ads2.read_sequence(CH_SEQUENCE,data_array)
		adjustedtime = time.time()-start
		print(value)