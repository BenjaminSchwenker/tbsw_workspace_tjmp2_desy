"""
  Script generating a ChargeCalibrationDB file 
  with the structure as it is used for the 
  PixelChargeCalibrator processor.

  Calibration function and its parameters are stored in 
  folders in the TFile. The folder names are build by:
  d + sensorID (i.e. d1, d21, ...)
  (d for detector)

  Sensors which do not have calibrations provided 
  do not get calibrated.

  The function parameters are  binned in pixel of the sensor (column, row).

  Usage: python3 calibFuncExample.py -dut W -geoID

  author: Benjamin Schwenker
  email: benjamin.schwenker@phys.uni-goettingen.de

  author: Helge Christoph Beck
  email: helge-christoph.beck@phys.uni-goettingen.de
"""

from ROOT import TFile, TF1, TH2F
import argparse

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser('calibFuncExample.py')
    add_arg = parser.add_argument
    add_arg('-dut', default="DUT", type=str, help='Name of sensor device')
    add_arg('-output', default='./calibrationDBFile.root', type=str, help='Path to output DB')
    add_arg('-geoID', default=-1, type=int, help='GeoID: integer')
    return parser.parse_args()

if __name__ == '__main__':

  # Parse the command line
  args = parse_args()
  
  # parameters to provide
  cols = 512
  rows = 512

  sensorIDList = [22]
  
  baseCalibFuncName = "calibFunc"
  baseCalibParaName = "para"

  gainCalibrationFileName = args.output
  dut = args.dut

  # generating file structure
  foutfile = TFile(gainCalibrationFileName, "RECREATE")
  
  for sensorID in sensorIDList:
    foutfile.cd()
    detDir = foutfile.mkdir("d" + str(sensorID)) # creating folder for sensor
    detDir.cd()
    funcName = baseCalibFuncName # function name is the same for all sensors in the file, differentiated by the folders
    fucalib = TF1(funcName, "pol2", -1.0, 100.0) # creating calibration function, use whatever you need as function and range
    # setting base parameters could be needed for non standard functions. Consult the TF1 reference.
    fucalib.Draw()
    fucalib.Write()

    nparFunc = fucalib.GetNpar()

    for par in range(nparFunc):
      histoParaName = baseCalibParaName + "_" + str(par) # same name for all sensors but in different folder
      hpara = TH2F(histoParaName, "", cols, 0, cols, rows, 0, rows) # creating histogram for parameters

      weight = par + 1 # get your parameters from a dedicated calibration probably
      for c in range(cols):
        for r in range(rows):
          hpara.Fill(c, r, 0)
      hpara.Write()

  foutfile.Close()
