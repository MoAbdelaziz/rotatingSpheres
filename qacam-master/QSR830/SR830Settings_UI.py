# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SR830Settings_UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SR830Settings(object):
    def setupUi(self, SR830Settings):
        SR830Settings.setObjectName("SR830Settings")
        SR830Settings.resize(297, 448)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(SR830Settings)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frameInputConfiguration = QtWidgets.QFrame(SR830Settings)
        self.frameInputConfiguration.setFrameShape(QtWidgets.QFrame.Panel)
        self.frameInputConfiguration.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameInputConfiguration.setLineWidth(2)
        self.frameInputConfiguration.setObjectName("frameInputConfiguration")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frameInputConfiguration)
        self.verticalLayout_2.setContentsMargins(4, 2, 4, 2)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelInputConfiguration = QtWidgets.QLabel(self.frameInputConfiguration)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelInputConfiguration.setFont(font)
        self.labelInputConfiguration.setObjectName("labelInputConfiguration")
        self.verticalLayout_2.addWidget(self.labelInputConfiguration)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.labelInput = QtWidgets.QLabel(self.frameInputConfiguration)
        self.labelInput.setObjectName("labelInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelInput)
        self.input = QtWidgets.QComboBox(self.frameInputConfiguration)
        self.input.setObjectName("input")
        self.input.addItem("")
        self.input.addItem("")
        self.input.addItem("")
        self.input.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.input)
        self.labelGrounding = QtWidgets.QLabel(self.frameInputConfiguration)
        self.labelGrounding.setObjectName("labelGrounding")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelGrounding)
        self.grounding = QtWidgets.QComboBox(self.frameInputConfiguration)
        self.grounding.setObjectName("grounding")
        self.grounding.addItem("")
        self.grounding.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.grounding)
        self.labelCoupling = QtWidgets.QLabel(self.frameInputConfiguration)
        self.labelCoupling.setObjectName("labelCoupling")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelCoupling)
        self.coupling = QtWidgets.QComboBox(self.frameInputConfiguration)
        self.coupling.setObjectName("coupling")
        self.coupling.addItem("")
        self.coupling.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.coupling)
        self.labelTimeConstant = QtWidgets.QLabel(self.frameInputConfiguration)
        self.labelTimeConstant.setObjectName("labelTimeConstant")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelTimeConstant)
        self.timeConstant = QtWidgets.QComboBox(self.frameInputConfiguration)
        self.timeConstant.setObjectName("timeConstant")
        self.timeConstant.addItem("")
        self.timeConstant.addItem("")
        self.timeConstant.addItem("")
        self.timeConstant.addItem("")
        self.timeConstant.addItem("")
        self.timeConstant.addItem("")
        self.timeConstant.addItem("")
        self.timeConstant.addItem("")
        self.timeConstant.addItem("")
        self.timeConstant.addItem("")
        self.timeConstant.addItem("")
        self.timeConstant.addItem("")
        self.timeConstant.addItem("")
        self.timeConstant.addItem("")
        self.timeConstant.addItem("")
        self.timeConstant.addItem("")
        self.timeConstant.addItem("")
        self.timeConstant.addItem("")
        self.timeConstant.addItem("")
        self.timeConstant.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.timeConstant)
        self.labelSlope = QtWidgets.QLabel(self.frameInputConfiguration)
        self.labelSlope.setObjectName("labelSlope")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelSlope)
        self.slope = QtWidgets.QComboBox(self.frameInputConfiguration)
        self.slope.setObjectName("slope")
        self.slope.addItem("")
        self.slope.addItem("")
        self.slope.addItem("")
        self.slope.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.slope)
        self.labelSynchronous = QtWidgets.QLabel(self.frameInputConfiguration)
        self.labelSynchronous.setObjectName("labelSynchronous")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelSynchronous)
        self.synchronous = QtWidgets.QComboBox(self.frameInputConfiguration)
        self.synchronous.setObjectName("synchronous")
        self.synchronous.addItem("")
        self.synchronous.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.synchronous)
        self.labelSensitivity = QtWidgets.QLabel(self.frameInputConfiguration)
        self.labelSensitivity.setObjectName("labelSensitivity")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.labelSensitivity)
        self.sensitivity = QtWidgets.QComboBox(self.frameInputConfiguration)
        self.sensitivity.setObjectName("sensitivity")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.sensitivity.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.sensitivity)
        self.labelReserve = QtWidgets.QLabel(self.frameInputConfiguration)
        self.labelReserve.setObjectName("labelReserve")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.labelReserve)
        self.reserve = QtWidgets.QComboBox(self.frameInputConfiguration)
        self.reserve.setObjectName("reserve")
        self.reserve.addItem("")
        self.reserve.addItem("")
        self.reserve.addItem("")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.reserve)
        self.labelLineFilter = QtWidgets.QLabel(self.frameInputConfiguration)
        self.labelLineFilter.setObjectName("labelLineFilter")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.labelLineFilter)
        self.filter = QtWidgets.QComboBox(self.frameInputConfiguration)
        self.filter.setObjectName("filter")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.filter)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout_4.addWidget(self.frameInputConfiguration)
        self.frameAuto = QtWidgets.QFrame(SR830Settings)
        self.frameAuto.setFrameShape(QtWidgets.QFrame.Panel)
        self.frameAuto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameAuto.setLineWidth(2)
        self.frameAuto.setObjectName("frameAuto")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frameAuto)
        self.verticalLayout_3.setContentsMargins(4, 2, 4, 2)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frameAuto)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.autoButtons = QtWidgets.QWidget(self.frameAuto)
        self.autoButtons.setObjectName("autoButtons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.autoButtons)
        self.horizontalLayout.setContentsMargins(4, 2, 4, 2)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.autoGain = QtWidgets.QPushButton(self.autoButtons)
        self.autoGain.setObjectName("autoGain")
        self.horizontalLayout.addWidget(self.autoGain)
        self.autoReserve = QtWidgets.QPushButton(self.autoButtons)
        self.autoReserve.setObjectName("autoReserve")
        self.horizontalLayout.addWidget(self.autoReserve)
        self.autoPhase = QtWidgets.QPushButton(self.autoButtons)
        self.autoPhase.setObjectName("autoPhase")
        self.horizontalLayout.addWidget(self.autoPhase)
        self.verticalLayout_3.addWidget(self.autoButtons)
        self.verticalLayout_4.addWidget(self.frameAuto)
        self.frameReference = QtWidgets.QFrame(SR830Settings)
        self.frameReference.setFrameShape(QtWidgets.QFrame.Panel)
        self.frameReference.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameReference.setLineWidth(2)
        self.frameReference.setObjectName("frameReference")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frameReference)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelReference = QtWidgets.QLabel(self.frameReference)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelReference.setFont(font)
        self.labelReference.setObjectName("labelReference")
        self.verticalLayout.addWidget(self.labelReference)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setVerticalSpacing(0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.labelSource = QtWidgets.QLabel(self.frameReference)
        self.labelSource.setObjectName("labelSource")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelSource)
        self.source = QtWidgets.QComboBox(self.frameReference)
        self.source.setObjectName("source")
        self.source.addItem("")
        self.source.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.source)
        self.labelFrequency = QtWidgets.QLabel(self.frameReference)
        self.labelFrequency.setObjectName("labelFrequency")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelFrequency)
        self.labelAmplitude = QtWidgets.QLabel(self.frameReference)
        self.labelAmplitude.setObjectName("labelAmplitude")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelAmplitude)
        self.labelTrigger = QtWidgets.QLabel(self.frameReference)
        self.labelTrigger.setObjectName("labelTrigger")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelTrigger)
        self.trigger = QtWidgets.QComboBox(self.frameReference)
        self.trigger.setObjectName("trigger")
        self.trigger.addItem("")
        self.trigger.addItem("")
        self.trigger.addItem("")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.trigger)
        self.labelPhase = QtWidgets.QLabel(self.frameReference)
        self.labelPhase.setObjectName("labelPhase")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelPhase)
        self.labelHarmonic = QtWidgets.QLabel(self.frameReference)
        self.labelHarmonic.setObjectName("labelHarmonic")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelHarmonic)
        self.harmonic = QtWidgets.QSpinBox(self.frameReference)
        self.harmonic.setMinimum(1)
        self.harmonic.setMaximum(19999)
        self.harmonic.setObjectName("harmonic")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.harmonic)
        self.frequency = QtWidgets.QDoubleSpinBox(self.frameReference)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frequency.sizePolicy().hasHeightForWidth())
        self.frequency.setSizePolicy(sizePolicy)
        self.frequency.setDecimals(3)
        self.frequency.setMinimum(0.001)
        self.frequency.setMaximum(102000.0)
        self.frequency.setProperty("value", 1.0)
        self.frequency.setObjectName("frequency")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.frequency)
        self.amplitude = QtWidgets.QDoubleSpinBox(self.frameReference)
        self.amplitude.setDecimals(3)
        self.amplitude.setMinimum(0.004)
        self.amplitude.setMaximum(2.5)
        self.amplitude.setSingleStep(0.1)
        self.amplitude.setProperty("value", 1.0)
        self.amplitude.setObjectName("amplitude")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.amplitude)
        self.phase = QtWidgets.QDoubleSpinBox(self.frameReference)
        self.phase.setMinimum(-360.0)
        self.phase.setMaximum(729.99)
        self.phase.setObjectName("phase")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.phase)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.verticalLayout_4.addWidget(self.frameReference)
        self.frameInputConfiguration.raise_()
        self.frameReference.raise_()
        self.frameAuto.raise_()

        self.retranslateUi(SR830Settings)
        QtCore.QMetaObject.connectSlotsByName(SR830Settings)

    def retranslateUi(self, SR830Settings):
        _translate = QtCore.QCoreApplication.translate
        SR830Settings.setWindowTitle(_translate("SR830Settings", "SR830"))
        self.frameInputConfiguration.setStatusTip(_translate("SR830Settings", "SR830: Input Configuration"))
        self.labelInputConfiguration.setText(_translate("SR830Settings", "Input Configuration"))
        self.labelInput.setText(_translate("SR830Settings", "Input"))
        self.input.setItemText(0, _translate("SR830Settings", "A"))
        self.input.setItemText(1, _translate("SR830Settings", "A-B"))
        self.input.setItemText(2, _translate("SR830Settings", "I (1 MOhm)"))
        self.input.setItemText(3, _translate("SR830Settings", "I (100 MOhm)"))
        self.labelGrounding.setText(_translate("SR830Settings", "Grounding"))
        self.grounding.setItemText(0, _translate("SR830Settings", "Shield Floating"))
        self.grounding.setItemText(1, _translate("SR830Settings", "Shield Grounded"))
        self.labelCoupling.setText(_translate("SR830Settings", "Coupling"))
        self.coupling.setItemText(0, _translate("SR830Settings", "AC Coupling"))
        self.coupling.setItemText(1, _translate("SR830Settings", "DC Coupling"))
        self.labelTimeConstant.setText(_translate("SR830Settings", "Time Constant"))
        self.timeConstant.setItemText(0, _translate("SR830Settings", "10 µs"))
        self.timeConstant.setItemText(1, _translate("SR830Settings", "30 µs"))
        self.timeConstant.setItemText(2, _translate("SR830Settings", "100 µs"))
        self.timeConstant.setItemText(3, _translate("SR830Settings", "300 µs"))
        self.timeConstant.setItemText(4, _translate("SR830Settings", "1 ms"))
        self.timeConstant.setItemText(5, _translate("SR830Settings", "3 ms"))
        self.timeConstant.setItemText(6, _translate("SR830Settings", "10 ms"))
        self.timeConstant.setItemText(7, _translate("SR830Settings", "30 ms"))
        self.timeConstant.setItemText(8, _translate("SR830Settings", "100 ms"))
        self.timeConstant.setItemText(9, _translate("SR830Settings", "300 ms"))
        self.timeConstant.setItemText(10, _translate("SR830Settings", "1 s"))
        self.timeConstant.setItemText(11, _translate("SR830Settings", "3 s"))
        self.timeConstant.setItemText(12, _translate("SR830Settings", "10 s"))
        self.timeConstant.setItemText(13, _translate("SR830Settings", "30 s"))
        self.timeConstant.setItemText(14, _translate("SR830Settings", "100 s"))
        self.timeConstant.setItemText(15, _translate("SR830Settings", "300 s"))
        self.timeConstant.setItemText(16, _translate("SR830Settings", "1 ks"))
        self.timeConstant.setItemText(17, _translate("SR830Settings", "3 ks"))
        self.timeConstant.setItemText(18, _translate("SR830Settings", "10 ks"))
        self.timeConstant.setItemText(19, _translate("SR830Settings", "30 ks"))
        self.labelSlope.setText(_translate("SR830Settings", "Slope"))
        self.slope.setItemText(0, _translate("SR830Settings", "6 dB/oct"))
        self.slope.setItemText(1, _translate("SR830Settings", "12 dB/oct"))
        self.slope.setItemText(2, _translate("SR830Settings", "18 dB/oct"))
        self.slope.setItemText(3, _translate("SR830Settings", "24 dB/oct"))
        self.labelSynchronous.setText(_translate("SR830Settings", "Synchronous"))
        self.synchronous.setItemText(0, _translate("SR830Settings", "Filter Off"))
        self.synchronous.setItemText(1, _translate("SR830Settings", "Filter On"))
        self.labelSensitivity.setText(_translate("SR830Settings", "Sensitivity"))
        self.sensitivity.setItemText(0, _translate("SR830Settings", "2 nV/fA"))
        self.sensitivity.setItemText(1, _translate("SR830Settings", "5 nV/fA"))
        self.sensitivity.setItemText(2, _translate("SR830Settings", "10 nV/fA"))
        self.sensitivity.setItemText(3, _translate("SR830Settings", "20 nV/fA"))
        self.sensitivity.setItemText(4, _translate("SR830Settings", "50 nV/fA"))
        self.sensitivity.setItemText(5, _translate("SR830Settings", "100 nV/fA"))
        self.sensitivity.setItemText(6, _translate("SR830Settings", "200 nV/fA"))
        self.sensitivity.setItemText(7, _translate("SR830Settings", "500 nV/fA"))
        self.sensitivity.setItemText(8, _translate("SR830Settings", "1 µV/pA"))
        self.sensitivity.setItemText(9, _translate("SR830Settings", "2 µV/pA"))
        self.sensitivity.setItemText(10, _translate("SR830Settings", "5 µV/pA"))
        self.sensitivity.setItemText(11, _translate("SR830Settings", "10 µV/pA"))
        self.sensitivity.setItemText(12, _translate("SR830Settings", "20 µV/pA"))
        self.sensitivity.setItemText(13, _translate("SR830Settings", "50 µV/pA"))
        self.sensitivity.setItemText(14, _translate("SR830Settings", "100 µV/pA"))
        self.sensitivity.setItemText(15, _translate("SR830Settings", "200 µV/pA"))
        self.sensitivity.setItemText(16, _translate("SR830Settings", "500 µV/pA"))
        self.sensitivity.setItemText(17, _translate("SR830Settings", "1 mV/nA"))
        self.sensitivity.setItemText(18, _translate("SR830Settings", "2 mV/nA"))
        self.sensitivity.setItemText(19, _translate("SR830Settings", "5 mV/nA"))
        self.sensitivity.setItemText(20, _translate("SR830Settings", "10 mV/nA"))
        self.sensitivity.setItemText(21, _translate("SR830Settings", "20 mV/nA"))
        self.sensitivity.setItemText(22, _translate("SR830Settings", "50 mV/nA"))
        self.sensitivity.setItemText(23, _translate("SR830Settings", "100 mV/nA"))
        self.sensitivity.setItemText(24, _translate("SR830Settings", "200 mV/nA"))
        self.sensitivity.setItemText(25, _translate("SR830Settings", "500 mV/nA"))
        self.sensitivity.setItemText(26, _translate("SR830Settings", "1 V/µA"))
        self.labelReserve.setText(_translate("SR830Settings", "Reserve"))
        self.reserve.setItemText(0, _translate("SR830Settings", "High"))
        self.reserve.setItemText(1, _translate("SR830Settings", "Normal"))
        self.reserve.setItemText(2, _translate("SR830Settings", "Low Noise"))
        self.labelLineFilter.setText(_translate("SR830Settings", "Line Filter"))
        self.filter.setItemText(0, _translate("SR830Settings", "No Filter"))
        self.filter.setItemText(1, _translate("SR830Settings", "Line Notch"))
        self.filter.setItemText(2, _translate("SR830Settings", "2x Line Notch"))
        self.filter.setItemText(3, _translate("SR830Settings", "Both"))
        self.frameAuto.setStatusTip(_translate("SR830Settings", "SR830: Automatic Settings"))
        self.label.setText(_translate("SR830Settings", "Auto"))
        self.autoGain.setText(_translate("SR830Settings", "Gain"))
        self.autoReserve.setText(_translate("SR830Settings", "Reserve"))
        self.autoPhase.setText(_translate("SR830Settings", "Phase"))
        self.frameReference.setStatusTip(_translate("SR830Settings", "SR830 Reference Signal"))
        self.labelReference.setText(_translate("SR830Settings", "Reference"))
        self.labelSource.setText(_translate("SR830Settings", "Source"))
        self.source.setItemText(0, _translate("SR830Settings", "External"))
        self.source.setItemText(1, _translate("SR830Settings", "Internal"))
        self.labelFrequency.setText(_translate("SR830Settings", "Frequency "))
        self.labelAmplitude.setText(_translate("SR830Settings", "Amplitude"))
        self.labelTrigger.setText(_translate("SR830Settings", "Trigger"))
        self.trigger.setItemText(0, _translate("SR830Settings", "Sine Zero Crossing"))
        self.trigger.setItemText(1, _translate("SR830Settings", "TTL Rising Edge"))
        self.trigger.setItemText(2, _translate("SR830Settings", "TTL Falling Edge"))
        self.labelPhase.setText(_translate("SR830Settings", "Phase"))
        self.labelHarmonic.setText(_translate("SR830Settings", "Harmonic"))
        self.frequency.setSuffix(_translate("SR830Settings", " Hz"))
        self.amplitude.setSuffix(_translate("SR830Settings", " Vrms"))
        self.phase.setSuffix(_translate("SR830Settings", "°"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SR830Settings = QtWidgets.QWidget()
    ui = Ui_SR830Settings()
    ui.setupUi(SR830Settings)
    SR830Settings.show()
    sys.exit(app.exec_())
