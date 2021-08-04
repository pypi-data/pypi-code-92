# -*- coding: utf-8 -*-
from aqt.utils import tr


# Form implementation generated from reading ui file 'qt/aqt/forms/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(667, 570)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 0))
        MainWindow.setWindowTitle("Anki")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/anki.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 667, 24))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuCol = QtWidgets.QMenu(self.menubar)
        self.menuCol.setObjectName("menuCol")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setShortcut("Ctrl+Q")
        self.actionExit.setObjectName("actionExit")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setShortcut("Ctrl+P")
        self.actionPreferences.setMenuRole(QtWidgets.QAction.PreferencesRole)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setMenuRole(QtWidgets.QAction.AboutRole)
        self.actionAbout.setObjectName("actionAbout")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setEnabled(False)
        self.actionUndo.setShortcut("Ctrl+Z")
        self.actionUndo.setObjectName("actionUndo")
        self.actionCheckMediaDatabase = QtWidgets.QAction(MainWindow)
        self.actionCheckMediaDatabase.setObjectName("actionCheckMediaDatabase")
        self.actionOpenPluginFolder = QtWidgets.QAction(MainWindow)
        self.actionOpenPluginFolder.setObjectName("actionOpenPluginFolder")
        self.actionDonate = QtWidgets.QAction(MainWindow)
        self.actionDonate.setObjectName("actionDonate")
        self.actionDownloadSharedPlugin = QtWidgets.QAction(MainWindow)
        self.actionDownloadSharedPlugin.setStatusTip("")
        self.actionDownloadSharedPlugin.setObjectName("actionDownloadSharedPlugin")
        self.actionFullDatabaseCheck = QtWidgets.QAction(MainWindow)
        self.actionFullDatabaseCheck.setObjectName("actionFullDatabaseCheck")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setShortcut("F1")
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionSwitchProfile = QtWidgets.QAction(MainWindow)
        self.actionSwitchProfile.setShortcut("Ctrl+Shift+P")
        self.actionSwitchProfile.setObjectName("actionSwitchProfile")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setShortcut("Ctrl+E")
        self.actionExport.setObjectName("actionExport")
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setShortcut("Ctrl+Shift+I")
        self.actionImport.setObjectName("actionImport")
        self.actionStudyDeck = QtWidgets.QAction(MainWindow)
        self.actionStudyDeck.setShortcut("/")
        self.actionStudyDeck.setObjectName("actionStudyDeck")
        self.actionEmptyCards = QtWidgets.QAction(MainWindow)
        self.actionEmptyCards.setObjectName("actionEmptyCards")
        self.actionCreateFiltered = QtWidgets.QAction(MainWindow)
        self.actionCreateFiltered.setShortcut("F")
        self.actionCreateFiltered.setObjectName("actionCreateFiltered")
        self.actionNoteTypes = QtWidgets.QAction(MainWindow)
        self.actionNoteTypes.setShortcut("Ctrl+Shift+N")
        self.actionNoteTypes.setObjectName("actionNoteTypes")
        self.actionAdd_ons = QtWidgets.QAction(MainWindow)
        self.actionAdd_ons.setShortcut("Ctrl+Shift+A")
        self.actionAdd_ons.setObjectName("actionAdd_ons")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setEnabled(False)
        self.actionRedo.setShortcut("Ctrl+Shift+Z")
        self.actionRedo.setObjectName("actionRedo")
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionDonate)
        self.menuHelp.addAction(self.actionAbout)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuCol.addAction(self.actionSwitchProfile)
        self.menuCol.addSeparator()
        self.menuCol.addAction(self.actionImport)
        self.menuCol.addAction(self.actionExport)
        self.menuCol.addSeparator()
        self.menuCol.addAction(self.actionExit)
        self.menuTools.addAction(self.actionStudyDeck)
        self.menuTools.addAction(self.actionCreateFiltered)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionFullDatabaseCheck)
        self.menuTools.addAction(self.actionCheckMediaDatabase)
        self.menuTools.addAction(self.actionEmptyCards)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionAdd_ons)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionNoteTypes)
        self.menuTools.addAction(self.actionPreferences)
        self.menubar.addAction(self.menuCol.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.menuHelp.setTitle(tr.qt_accel_help())
        self.menuEdit.setTitle(tr.qt_accel_edit())
        self.menuCol.setTitle(tr.qt_accel_file())
        self.menuTools.setTitle(tr.qt_accel_tools())
        self.actionExit.setText(tr.qt_accel_exit())
        self.actionPreferences.setText(tr.qt_accel_preferences())
        self.actionPreferences.setStatusTip(tr.qt_misc_configure_interface_language_and_options())
        self.actionAbout.setText(tr.qt_accel_about())
        self.actionUndo.setText(tr.qt_accel_undo())
        self.actionCheckMediaDatabase.setText(tr.qt_accel_check_media())
        self.actionCheckMediaDatabase.setStatusTip(tr.qt_misc_check_the_files_in_the_media())
        self.actionOpenPluginFolder.setText(tr.qt_accel_open_addons_folder())
        self.actionDonate.setText(tr.qt_accel_support_anki())
        self.actionDownloadSharedPlugin.setText(tr.qt_accel_browse_and_install())
        self.actionFullDatabaseCheck.setText(tr.qt_accel_check_database())
        self.actionDocumentation.setText(tr.qt_accel_guide())
        self.actionSwitchProfile.setText(tr.qt_accel_switch_profile())
        self.actionExport.setText(tr.qt_accel_export())
        self.actionImport.setText(tr.qt_accel_import())
        self.actionStudyDeck.setText(tr.qt_misc_study_deck())
        self.actionEmptyCards.setText(tr.qt_misc_empty_cards())
        self.actionCreateFiltered.setText(tr.qt_misc_create_filtered_deck())
        self.actionNoteTypes.setText(tr.qt_misc_manage_note_types())
        self.actionAdd_ons.setText(tr.qt_misc_addons())
        self.actionRedo.setText(tr.qt_accel_redo())
from . import icons_rc