# -*- coding: utf-8 -*-
from aqt.utils import tr


# Form implementation generated from reading ui file 'qt/aqt/forms/dconf.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(638, 514)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_31 = QtWidgets.QLabel(Dialog)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_2.addWidget(self.label_31)
        self.dconf = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dconf.sizePolicy().hasHeightForWidth())
        self.dconf.setSizePolicy(sizePolicy)
        self.dconf.setObjectName("dconf")
        self.horizontalLayout_2.addWidget(self.dconf)
        self.confOpts = QtWidgets.QToolButton(Dialog)
        self.confOpts.setMaximumSize(QtCore.QSize(16777215, 32))
        self.confOpts.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.confOpts.setArrowType(QtCore.Qt.NoArrow)
        self.confOpts.setObjectName("confOpts")
        self.horizontalLayout_2.addWidget(self.confOpts)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.count = QtWidgets.QLabel(Dialog)
        self.count.setStyleSheet("* { color: red }")
        self.count.setText("")
        self.count.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        self.count.setWordWrap(True)
        self.count.setObjectName("count")
        self.verticalLayout.addWidget(self.count)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(12)
        self.gridLayout.setObjectName("gridLayout")
        self.label_24 = QtWidgets.QLabel(self.tab)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 5, 0, 1, 1)
        self.lrnFactor = QtWidgets.QSpinBox(self.tab)
        self.lrnFactor.setSuffix("%")
        self.lrnFactor.setMinimum(131)
        self.lrnFactor.setMaximum(999)
        self.lrnFactor.setProperty("value", 250)
        self.lrnFactor.setObjectName("lrnFactor")
        self.gridLayout.addWidget(self.lrnFactor, 5, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.lrnEasyInt = QtWidgets.QSpinBox(self.tab)
        self.lrnEasyInt.setMinimum(1)
        self.lrnEasyInt.setObjectName("lrnEasyInt")
        self.gridLayout.addWidget(self.lrnEasyInt, 4, 1, 1, 1)
        self.lrnGradInt = QtWidgets.QSpinBox(self.tab)
        self.lrnGradInt.setMinimum(1)
        self.lrnGradInt.setObjectName("lrnGradInt")
        self.gridLayout.addWidget(self.lrnGradInt, 3, 1, 1, 1)
        self.newplim = QtWidgets.QLabel(self.tab)
        self.newplim.setText("")
        self.newplim.setObjectName("newplim")
        self.gridLayout.addWidget(self.newplim, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.newPerDay = QtWidgets.QSpinBox(self.tab)
        self.newPerDay.setMaximum(9999)
        self.newPerDay.setObjectName("newPerDay")
        self.gridLayout.addWidget(self.newPerDay, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.lrnSteps = QtWidgets.QLineEdit(self.tab)
        self.lrnSteps.setObjectName("lrnSteps")
        self.gridLayout.addWidget(self.lrnSteps, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.newOrder = QtWidgets.QComboBox(self.tab)
        self.newOrder.setObjectName("newOrder")
        self.gridLayout.addWidget(self.newOrder, 1, 1, 1, 2)
        self.bury = QtWidgets.QCheckBox(self.tab)
        self.bury.setObjectName("bury")
        self.gridLayout.addWidget(self.bury, 6, 0, 1, 3)
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(12)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_20 = QtWidgets.QLabel(self.tab_3)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 1, 0, 1, 1)
        self.easyBonus = QtWidgets.QSpinBox(self.tab_3)
        self.easyBonus.setSuffix("%")
        self.easyBonus.setMinimum(100)
        self.easyBonus.setMaximum(1000)
        self.easyBonus.setSingleStep(5)
        self.easyBonus.setObjectName("easyBonus")
        self.gridLayout_3.addWidget(self.easyBonus, 1, 1, 1, 1)
        self.revPerDay = QtWidgets.QSpinBox(self.tab_3)
        self.revPerDay.setMinimum(0)
        self.revPerDay.setMaximum(9999)
        self.revPerDay.setObjectName("revPerDay")
        self.gridLayout_3.addWidget(self.revPerDay, 0, 1, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.tab_3)
        self.label_33.setObjectName("label_33")
        self.gridLayout_3.addWidget(self.label_33, 2, 0, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.tab_3)
        self.label_37.setObjectName("label_37")
        self.gridLayout_3.addWidget(self.label_37, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)
        self.maxIvl = QtWidgets.QSpinBox(self.tab_3)
        self.maxIvl.setSuffix("")
        self.maxIvl.setMinimum(1)
        self.maxIvl.setMaximum(99999)
        self.maxIvl.setObjectName("maxIvl")
        self.gridLayout_3.addWidget(self.maxIvl, 3, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.tab_3)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 3, 2, 1, 1)
        self.revplim = QtWidgets.QLabel(self.tab_3)
        self.revplim.setText("")
        self.revplim.setObjectName("revplim")
        self.gridLayout_3.addWidget(self.revplim, 0, 2, 1, 1)
        self.fi1 = QtWidgets.QDoubleSpinBox(self.tab_3)
        self.fi1.setSuffix("%")
        self.fi1.setDecimals(0)
        self.fi1.setMinimum(0.0)
        self.fi1.setMaximum(999.0)
        self.fi1.setSingleStep(1.0)
        self.fi1.setProperty("value", 100.0)
        self.fi1.setObjectName("fi1")
        self.gridLayout_3.addWidget(self.fi1, 2, 1, 1, 1)
        self.buryRev = QtWidgets.QCheckBox(self.tab_3)
        self.buryRev.setObjectName("buryRev")
        self.gridLayout_3.addWidget(self.buryRev, 5, 0, 1, 3)
        self.hardFactorLabel = QtWidgets.QLabel(self.tab_3)
        self.hardFactorLabel.setObjectName("hardFactorLabel")
        self.gridLayout_3.addWidget(self.hardFactorLabel, 4, 0, 1, 1)
        self.hardFactor = QtWidgets.QSpinBox(self.tab_3)
        self.hardFactor.setSuffix("%")
        self.hardFactor.setMinimum(5)
        self.hardFactor.setMaximum(120)
        self.hardFactor.setObjectName("hardFactor")
        self.gridLayout_3.addWidget(self.hardFactor, 4, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 152, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(12)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 0, 0, 1, 1)
        self.lapSteps = QtWidgets.QLineEdit(self.tab_2)
        self.lapSteps.setObjectName("lapSteps")
        self.gridLayout_2.addWidget(self.lapSteps, 0, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)
        self.leechThreshold = QtWidgets.QSpinBox(self.tab_2)
        self.leechThreshold.setObjectName("leechThreshold")
        self.gridLayout_2.addWidget(self.leechThreshold, 3, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 3, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 4, 0, 1, 1)
        self.lapMinInt = QtWidgets.QSpinBox(self.tab_2)
        self.lapMinInt.setMinimum(1)
        self.lapMinInt.setMaximum(99)
        self.lapMinInt.setObjectName("lapMinInt")
        self.gridLayout_2.addWidget(self.lapMinInt, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 2, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 2, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leechAction = QtWidgets.QComboBox(self.tab_2)
        self.leechAction.setObjectName("leechAction")
        self.leechAction.addItem("")
        self.leechAction.addItem("")
        self.horizontalLayout.addWidget(self.leechAction)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 1, 1, 2)
        self.lapMult = QtWidgets.QSpinBox(self.tab_2)
        self.lapMult.setSuffix("%")
        self.lapMult.setMaximum(100)
        self.lapMult.setSingleStep(5)
        self.lapMult.setObjectName("lapMult")
        self.gridLayout_2.addWidget(self.lapMult, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 72, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_6.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSpacing(12)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_25 = QtWidgets.QLabel(self.tab_5)
        self.label_25.setObjectName("label_25")
        self.gridLayout_5.addWidget(self.label_25, 0, 0, 1, 1)
        self.maxTaken = QtWidgets.QSpinBox(self.tab_5)
        self.maxTaken.setMinimum(30)
        self.maxTaken.setMaximum(3600)
        self.maxTaken.setSingleStep(10)
        self.maxTaken.setObjectName("maxTaken")
        self.gridLayout_5.addWidget(self.maxTaken, 0, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.tab_5)
        self.label_26.setObjectName("label_26")
        self.gridLayout_5.addWidget(self.label_26, 0, 2, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_5)
        self.showTimer = QtWidgets.QCheckBox(self.tab_5)
        self.showTimer.setObjectName("showTimer")
        self.verticalLayout_6.addWidget(self.showTimer)
        self.autoplaySounds = QtWidgets.QCheckBox(self.tab_5)
        self.autoplaySounds.setObjectName("autoplaySounds")
        self.verticalLayout_6.addWidget(self.autoplaySounds)
        self.replayQuestion = QtWidgets.QCheckBox(self.tab_5)
        self.replayQuestion.setChecked(False)
        self.replayQuestion.setObjectName("replayQuestion")
        self.verticalLayout_6.addWidget(self.replayQuestion)
        spacerItem4 = QtWidgets.QSpacerItem(20, 199, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Help|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.RestoreDefaults)  # type: ignore
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)  # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.dconf, self.confOpts)
        Dialog.setTabOrder(self.confOpts, self.tabWidget)
        Dialog.setTabOrder(self.tabWidget, self.lrnSteps)
        Dialog.setTabOrder(self.lrnSteps, self.newOrder)
        Dialog.setTabOrder(self.newOrder, self.newPerDay)
        Dialog.setTabOrder(self.newPerDay, self.lrnGradInt)
        Dialog.setTabOrder(self.lrnGradInt, self.lrnEasyInt)
        Dialog.setTabOrder(self.lrnEasyInt, self.lrnFactor)
        Dialog.setTabOrder(self.lrnFactor, self.bury)
        Dialog.setTabOrder(self.bury, self.revPerDay)
        Dialog.setTabOrder(self.revPerDay, self.easyBonus)
        Dialog.setTabOrder(self.easyBonus, self.fi1)
        Dialog.setTabOrder(self.fi1, self.maxIvl)
        Dialog.setTabOrder(self.maxIvl, self.hardFactor)
        Dialog.setTabOrder(self.hardFactor, self.buryRev)
        Dialog.setTabOrder(self.buryRev, self.lapSteps)
        Dialog.setTabOrder(self.lapSteps, self.lapMult)
        Dialog.setTabOrder(self.lapMult, self.lapMinInt)
        Dialog.setTabOrder(self.lapMinInt, self.leechThreshold)
        Dialog.setTabOrder(self.leechThreshold, self.leechAction)
        Dialog.setTabOrder(self.leechAction, self.maxTaken)
        Dialog.setTabOrder(self.maxTaken, self.showTimer)
        Dialog.setTabOrder(self.showTimer, self.autoplaySounds)
        Dialog.setTabOrder(self.autoplaySounds, self.replayQuestion)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.label_31.setText(tr.scheduling_options_group())
        self.confOpts.setText(tr.actions_manage())
        self.label_24.setText(tr.scheduling_starting_ease())
        self.label_8.setText(tr.scheduling_order())
        self.label_5.setText(tr.scheduling_easy_interval())
        self.label_4.setText(tr.scheduling_graduating_interval())
        self.label_6.setText(tr.scheduling_new_cardsday())
        self.label_2.setText(tr.scheduling_steps_in_minutes())
        self.bury.setText(tr.scheduling_bury_related_new_cards_until_the())
        self.label_9.setText(tr.scheduling_days())
        self.label_7.setText(tr.scheduling_days())
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), tr.scheduling_new_cards())
        self.label_20.setText(tr.scheduling_easy_bonus())
        self.label_33.setText(tr.scheduling_interval_modifier())
        self.label_37.setText(tr.scheduling_maximum_reviewsday())
        self.label_3.setText(tr.scheduling_maximum_interval())
        self.label_23.setText(tr.scheduling_days())
        self.buryRev.setText(tr.scheduling_bury_related_reviews_until_the_next())
        self.hardFactorLabel.setText(tr.scheduling_hard_interval())
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), tr.scheduling_reviews())
        self.label_17.setText(tr.scheduling_steps_in_minutes())
        self.label.setText(tr.scheduling_new_interval())
        self.label_10.setText(tr.scheduling_leech_threshold())
        self.label_11.setText(tr.scheduling_lapses2())
        self.label_12.setText(tr.scheduling_leech_action())
        self.label_13.setText(tr.scheduling_minimum_interval())
        self.label_14.setText(tr.scheduling_days())
        self.leechAction.setItemText(0, tr.actions_suspend_card())
        self.leechAction.setItemText(1, tr.scheduling_tag_only())
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), tr.scheduling_lapses())
        self.label_25.setText(tr.scheduling_ignore_answer_times_longer_than())
        self.label_26.setText(tr.scheduling_seconds())
        self.showTimer.setText(tr.scheduling_show_answer_timer())
        self.autoplaySounds.setText(tr.scheduling_automatically_play_audio())
        self.replayQuestion.setText(tr.scheduling_always_include_question_side_when_replaying())
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), tr.scheduling_general())
from . import icons_rc