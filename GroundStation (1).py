from PyQt5 import QtCore, QtGui, QtWidgets,uic
from pyqtgraph import PlotWidget,setConfigOption,mkPen
from PyQt5.QtWebEngineWidgets import QWebEngineView
from geopy.geocoders import ArcGIS
import folium
import io
import csv
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread,QObject,pyqtSignal
from PyQt5.QtGui import QPen, QColor
import re


f=open("Simution_data.csv","r")
time=[]
altitude=[]
air_speed=[]
gps_altitude=[]
temperature=[]
voltage=[]
pressure=[]
setConfigOption('background', 'w')

r=csv.reader(f)
columns=next(r)
row=next(r)
packets=0


class Ui_MainWindow(object):

        def __init__(self,app):
                self.app=app



                self.ui=uic.loadUi("GroundStationGUI.ui")

                self.ui.ALT.setTitle("Altitude V/s Time",color="k", size="10pt")
                self.ui.AST.setTitle("AIR_SPEED V/s Time",color="k", size="10pt")
                self.ui.TEMPT.setTitle("TEMPERATURE V/s Time",color="k", size="10pt")
                self.ui.VT.setTitle("VOLTAGE V/s Time",color="k", size="10pt")
                self.ui.PT.setTitle("PRESSURE V/s Time",color="k", size="10pt")
                self.ui.TT.setTitle("GPS_ALTITUDE V/s Time",color="k", size="10pt")

                self.ui.csv_display.setRowCount(8000)
                self.ui.csv_display.setColumnCount(21)

                self.ui.command_enter_button.clicked.connect(self.command)
                self.ui.csv_convert.clicked.connect(self.convert_to_csv)

                self.ui.show()
                self.run()

        #printing text from command input
        def command(self):
                #print(self.ui.command_input.toPlainText())
                current_cmd=self.ui.command_input.toPlainText()
                self.ui.command_input.clear()

                cmd=current_cmd.split(",")
                cmd=cmd[2:]
                print(cmd)

                #CX - Payload Telemetry On/Off Command
                if cmd[0]=="CX":
                        if cmd[1]=="ON":
                                print("Transmitting")
                                self.plot_A2()

                        elif cmd[1]=="OFF":
                              print("Not Transmitting")
                              self.Pause()
                              self.map_plot()


                        else:
                              print("ERROR: INCORRECT INPUT")
                #ST - Set Time
                elif cmd[0]=="ST":
                        if re.match(r'^\d{2}-\d{2}-\d{4}$',cmd[1]):
                                print("New Time: ",cmd[1])
                        elif cmd[1]=="GPS":
                                print("New Time is GPS time")
                        else:
                                print("ERROR: INCORRECT INPUT")
                #SIM - Simulation Mode Control Command
                elif cmd[0]=="SIM":
                        flag1=False
                        flag2=False
                        if cmd[1]=="ENABLE":
                                flag1=True
                                print("Enabled")
                        elif cmd[1]=="ACTIVATE":
                                flag2=True
                                print("Activate")
                        elif cmd[1]=="DISABLE":
                                flag1=False
                                flag2=False
                                print("Disabled")
                        else:
                              print("ERROR: INCORRECT INPUT")

                        if flag1==True and flag2==True:
                                print("Simulation Mode Started")
                #SIMP - Simulated Pressure Data (to be used in Simulation Mode only)
                elif cmd[0]=="SIMP":
                        sim_pressure=cmd[1]
                        pressure=sim_pressure*(10**(-3))
                        print("Pressure:",pressure)
                #CAL - Calibrate Altitude to Zero
                elif cmd[0]=="CAL":
                        altitude=0
                        print("altitude:",altitude)
                #BCN - Control Audio Beacon
                elif cmd[0]=="BCN":
                        if cmd[1]=="ON":
                                print("Audio Beacon ON")
                        elif cmd[1]=="OFF":
                                print("Audio Beacon OFF")
                        else:
                              print("ERROR: INCORRECT INPUT")
                else:
                        print("Error")

        def plot_A2(self):
                def update_plot():
                        global row
                        try:
                                row=next(r)
                                #print(row)
                                time.append(float(row[21]))
                                altitude.append(float(row[5]))
                                air_speed.append(float(row[6]))
                                temperature.append(float(row[9]))
                                voltage.append(float(row[10]))
                                pressure.append(float(row[11]))
                                gps_altitude.append(float(row[13]))

                                self.refALT.setData(time,altitude)
                                self.refAIR_SPEED.setData(time,air_speed)
                                self.refTEMP.setData(time,temperature)
                                self.refVOLT.setData(time,voltage)
                                self.refPRESS.setData(time,pressure)
                                self.refT.setData(time,gps_altitude)

                                self.ui.L_MissionTime.setText(row[1])
                                self.ui.L_PacketCount.setText(row[2])
                                self.ui.L_Mode.setText(row[3])
                                self.ui.L_State.setText(row[4])
                                self.ui.L_altitude.setText(row[5])
                                self.ui.L_AirSpeed.setText(row[6])
                                self.ui.L_HS.setText(row[7])
                                self.ui.L_PS.setText(row[8])
                                self.ui.L_Temperature.setText(row[9])
                                self.ui.L_voltage.setText(row[10])
                                self.ui.L_AirPressure.setText(row[11])
                                self.ui.L_GPS_Time.setText(row[12])
                                self.ui.L_GPS_Altitude.setText(row[13])
                                self.ui.L_latitude.setText(row[14])
                                self.ui.L_longitude.setText(row[15])
                                self.ui.L_Sats.setText(row[16])
                                self.ui.L_tiltX.setText(row[17])
                                self.ui.L_tiltY.setText(row[18])
                                self.ui.L_rotZ.setText(row[19])
                                self.ui.L_echo.setText(row[20])

                                self.load_data()
                        except Exception as exc:
                                print(exc)

                self.Timer=QtCore.QTimer()
                self.Timer.setInterval(1000)
                self.Timer.timeout.connect(update_plot)
                self.Timer.start()

                #ALTITUDE VS TIME
                self.refALT=self.ui.ALT.plot(time,altitude,pen=mkPen(color='k',width=5))
                self.set_axis_color(self.ui.ALT)

                #AIR_SPEED V/s Time
                self.refAIR_SPEED=self.ui.AST.plot(time,air_speed,pen=mkPen(color='r',width=5))
                self.set_axis_color(self.ui.AST)

                #TEMPERATURE V/s Time
                self.refTEMP=self.ui.TEMPT.plot(time,temperature,pen=mkPen(color='g',width=5))
                self.set_axis_color(self.ui.TEMPT)

                #VOLTAGE V/s Time
                self.refVOLT=self.ui.VT.plot(time,voltage,pen=mkPen(color='b',width=5))
                self.set_axis_color(self.ui.VT)

                #PRESSURE V/s Time
                self.refPRESS=self.ui.PT.plot(time,pressure,pen=mkPen(color='m',width=5))
                self.set_axis_color(self.ui.PT)

                #Thrust V/s Time
                self.refT=self.ui.TT.plot(time,gps_altitude,pen=mkPen(color='orange',width=5))
                self.set_axis_color(self.ui.TT)

        def set_axis_color(self, plot_widget):
                # Set axis color to black
                axis_color = QColor(0, 0, 0)  # Black color

                # Set axis pen color
                y_axis = plot_widget.getAxis("left")
                x_axis = plot_widget.getAxis("bottom")
                y_axis.setPen(axis_color)
                x_axis.setPen(axis_color)

                y_axis.setTickPen(axis_color, width=3)
                x_axis.setTickPen(axis_color, width=3)

                # Set tick text color
                y_axis.setTextPen(axis_color)
                x_axis.setTextPen(axis_color)

        def Pause(self):
                #print(row)
                self.Timer.stop() #PAUSES PLOTTING!!!!!!!!!!!!!!!!!!!!!

        def load_data(self):
                global row
                global packets
                for i in row:
                        for j in range(0,21):
                                self.ui.csv_display.setItem(packets,j,QTableWidgetItem(str(row[j])))
                packets+=1

        def convert_to_csv(self):
                try:
                        with open('data_packets.csv', 'w', newline='') as csvfile:
                                writer = csv.writer(csvfile)
                                writer.writerow(columns)

                                # Write received data from the csv_display table
                                for row_index in range(self.ui.csv_display.rowCount()):
                                        row_data = []
                                        for col_index in range(self.ui.csv_display.columnCount()):
                                                item = self.ui.csv_display.item(row_index, col_index)
                                                if item is not None:
                                                        row_data.append(item.text())
                                                else:
                                                        row_data.append("")  # Handle empty cells
                                        writer.writerow(row_data)
                                print("Data from csv_display converted to CSV: simulation_results.csv")

                except Exception as exc:
                        print("Error while converting to CSV:", exc)


        def map_plot(self):
                nom=ArcGIS()
                gps=nom.geocode("Vellore")
                gps_latitude=gps.latitude
                gps_longitude=gps.longitude
                map=folium.Map(location=[gps_latitude,gps_longitude],zoom_start=12)#zoom_start(default)=10
                map.add_child(folium.Marker(location=[gps_latitude,gps_longitude],icon=folium.Icon(color="red"),popup="CanSat"))
                map_data=io.BytesIO()
                map.save(map_data,close_file=False)
                self.ui.map_display.setHtml(map_data.getvalue().decode())

        def run(self):
                self.app.exec_()

        ###

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui_MainWindow(app)