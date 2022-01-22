#!/usr/bin/python
"""
Contains command mneonics for the ThorLabs APT protocol

Class originally contributed by Catherine Holloway.
"""

# IMPORTS #####################################################################

from enum import IntEnum

# CLASSES #####################################################################


class ThorLabsCommands(IntEnum):
    """
    Enum containing command mneonics for the ThorLabs APT protocol
    """

    # General System Commands
    MOD_IDENTIFY = 0x0223
    MOD_SET_CHANENABLESTATE = 0x0210
    MOD_REQ_CHANENABLESTATE = 0x0211
    MOD_GET_CHANENABLESTATE = 0x0212
    HW_DISCONNECT = 0x0002
    HW_RESPONSE = 0x0080
    HW_RICHRESPONSE = 0x0081
    HW_START_UPDATEMSGS = 0x0011
    HW_STOP_UPDATEMSGS = 0x0012
    HW_REQ_INFO = 0x0005
    HW_GET_INFO = 0x0006
    RACK_REQ_BAYUSED = 0x0060
    RACK_GET_BAYUSED = 0x0061
    HUB_REQ_BAYUSED = 0x0065
    HUB_GET_BAYUSED = 0x0066
    RACK_REQ_STATUSBITS = 0x0226
    RACK_GET_STATUSBITS = 0x0227
    RACK_SET_DIGOUTPUTS = 0x0228
    RACK_REQ_DIGOUTPUTS = 0x0229
    RACK_GET_DIGOUTPUTS = 0x0230
    MOD_SET_DIGOUTPUTS = 0x0213
    MOD_REQ_DIGOUTPUTS = 0x0214
    MOD_GET_DIGOUTPUTS = 0x0215

    # Motor Control Messages
    MOT_SET_POSCOUNTER = 0x0410
    MOT_REQ_POSCOUNTER = 0x0411
    MOT_GET_POSCOUNTER = 0x0412
    MOT_SET_ENCCOUNTER = 0x0409
    MOT_REQ_ENCCOUNTER = 0x040A
    MOT_GET_ENCCOUNTER = 0x040B
    MOT_SET_VELPARAMS = 0x0413
    MOT_REQ_VELPARAMS = 0x0414
    MOT_GET_VELPARAMS = 0x0415
    MOT_SET_JOGPARAMS = 0x0416
    MOT_REQ_JOGPARAMS = 0x0417
    MOT_GET_JOGPARAMS = 0x0418
    MOT_REQ_ADCINPUTS = 0x042B
    MOT_GET_ADCINPUTS = 0x042C
    MOT_SET_POWERPARAMS = 0x0426
    MOT_REQ_POWERPARAMS = 0x0427
    MOT_GET_POWERPARAMS = 0x0428
    MOT_SET_GENMOVEPARAMS = 0x043A
    MOT_REQ_GENMOVEPARAMS = 0x043B
    MOT_GET_GENMOVEPARAMS = 0x043C
    MOT_SET_MOVERELPARAMS = 0x0445
    MOT_REQ_MOVERELPARAMS = 0x0446
    MOT_GET_MOVERELPARAMS = 0x0447
    MOT_SET_MOVEABSPARAMS = 0x0450
    MOT_REQ_MOVEABSPARAMS = 0x0451
    MOT_GET_MOVEABSPARAMS = 0x0452
    MOT_SET_HOMEPARAMS = 0x0440
    MOT_REQ_HOMEPARAMS = 0x0441
    MOT_GET_HOMEPARAMS = 0x0442
    MOT_SET_LIMSWITCHPARAMS = 0x0423
    MOT_REQ_LIMSWITCHPARAMS = 0x0424
    MOT_GET_LIMSWITCHPARAMS = 0x0425
    MOT_MOVE_HOME = 0x0443
    MOT_MOVE_HOMED = 0x0444
    MOT_MOVE_RELATIVE = 0x0448
    MOT_MOVE_COMPLETED = 0x0464
    MOT_MOVE_ABSOLUTE = 0x0453
    MOT_MOVE_JOG = 0x046A
    MOT_MOVE_VELOCITY = 0x0457
    MOT_MOVE_STOP = 0x0465
    MOT_MOVE_STOPPED = 0x0466
    MOT_SET_DCPIDPARAMS = 0x04A0
    MOT_REQ_DCPIDPARAMS = 0x04A1
    MOT_GET_DCPIDPARAMS = 0x04A2
    MOT_SET_AVMODES = 0x04B3
    MOT_REQ_AVMODES = 0x04B4
    MOT_GET_AVMODES = 0x04B5
    MOT_SET_POTPARAMS = 0x04B0
    MOT_REQ_POTPARAMS = 0x04B1
    MOT_GET_POTPARAMS = 0x04B2
    MOT_SET_BUTTONPARAMS = 0x04B6
    MOT_REQ_BUTTONPARAMS = 0x04B7
    MOT_GET_BUTTONPARAMS = 0x04B8
    MOT_SET_EEPROMPARAMS = 0x04B9
    MOT_SET_PMDPOSITIONLOOPPARAMS = 0x04D7
    MOT_REQ_PMDPOSITIONLOOPPARAMS = 0x04D8
    MOT_GET_PMDPOSITIONLOOPPARAMS = 0x04D9
    MOT_SET_PMDMOTOROUTPUTPARAMS = 0x04DA
    MOT_REQ_PMDMOTOROUTPUTPARAMS = 0x04DB
    MOT_GET_PMDMOTOROUTPUTPARAMS = 0x04DC
    MOT_SET_PMDTRACKSETTLEPARAMS = 0x04E0
    MOT_REQ_PMDTRACKSETTLEPARAMS = 0x04E1
    MOT_GET_PMDTRACKSETTLEPARAMS = 0x04E2
    MOT_SET_PMDPROFILEMODEPARAMS = 0x04E3
    MOT_REQ_PMDPROFILEMODEPARAMS = 0x04E4
    MOT_GET_PMDPROFILEMODEPARAMS = 0x04E5
    MOT_SET_PMDJOYSTICKPARAMS = 0x04E6
    MOT_REQ_PMDJOYSTICKPARAMS = 0x04E7
    MOT_GET_PMDJOYSTICKPARAMS = 0x04E8
    MOT_SET_PMDCURRENTLOOPPARAMS = 0x04D4
    MOT_REQ_PMDCURRENTLOOPPARAMS = 0x04D5
    MOT_GET_PMDCURRENTLOOPPARAMS = 0x04D6
    MOT_SET_PMDSETTLEDCURRENTLOOPPARAMS = 0x04E9
    MOT_REQ_PMDSETTLEDCURRENTLOOPPARAMS = 0x04EA
    MOT_GET_PMDSETTLEDCURRENTLOOPPARAMS = 0x04EB
    MOT_SET_PMDSTAGEAXISPARAMS = 0x04F0
    MOT_REQ_PMDSTAGEAXISPARAMS = 0x04F1
    MOT_GET_PMDSTAGEAXISPARAMS = 0x04F2
    MOT_GET_STATUSUPDATE = 0x0481
    MOT_REQ_STATUSUPDATE = 0x0480
    MOT_GET_DCSTATUSUPDATE = 0x0491
    MOT_REQ_DCSTATUSUPDATE = 0x0490
    MOT_ACK_DCSTATUSUPDATE = 0x0492
    MOT_REQ_STATUSBITS = 0x0429
    MOT_GET_STATUSBITS = 0x042A
    MOT_SUSPEND_ENDOFMOVEMSGS = 0x046B
    MOT_RESUME_ENDOFMOVEMSGS = 0x046C
    MOT_SET_TRIGGER = 0x0500
    MOT_REQ_TRIGGER = 0x0501
    MOT_GET_TRIGGER = 0x0502

    # Solenoid Control Messages
    MOT_SET_SOL_OPERATINGMODE = 0x04C0
    MOT_REQ_SOL_OPERATINGMODE = 0x04C1
    MOT_GET_SOL_OPERATINGMODE = 0x04C2
    MOT_SET_SOL_CYCLEPARAMS = 0x04C3
    MOT_REQ_SOL_CYCLEPARAMS = 0x04C4
    MOT_GET_SOL_CYCLEPARAMS = 0x04C5
    MOT_SET_SOL_INTERLOCKMODE = 0x04C6
    MOT_REQ_SOL_INTERLOCKMODE = 0x04C7
    MOT_GET_SOL_INTERLOCKMODE = 0x04C8
    MOT_SET_SOL_STATE = 0x04CB
    MOT_REQ_SOL_STATE = 0x04CC
    MOT_GET_SOL_STATE = 0x04CD

    # Piezo Control Messages
    PZ_SET_POSCONTROLMODE = 0x0640
    PZ_REQ_POSCONTROLMODE = 0x0641
    PZ_GET_POSCONTROLMODE = 0x0642
    PZ_SET_OUTPUTVOLTS = 0x0643
    PZ_REQ_OUTPUTVOLTS = 0x0644
    PZ_GET_OUTPUTVOLTS = 0x0645
    PZ_SET_OUTPUTPOS = 0x0646
    PZ_REQ_OUTPUTPOS = 0x0647
    PZ_GET_OUTPUTPOS = 0x0648
    PZ_SET_INPUTVOLTSSRC = 0x0652
    PZ_REQ_INPUTVOLTSSRC = 0x0653
    PZ_GET_INPUTVOLTSSRC = 0x0654
    PZ_SET_PICONSTS = 0x0655
    PZ_REQ_PICONSTS = 0x0656
    PZ_GET_PICONSTS = 0x0657
    PZ_REQ_PZSTATUSBITS = 0x065B
    PZ_GET_PZSTATUSBITS = 0x065C
    PZ_GET_PZSTATUSUPDATE = 0x0661
    PZ_ACK_PZSTATUSUPDATE = 0x0662
    PZ_SET_OUTPUTLUT = 0x0700
    PZ_REQ_OUTPUTLUT = 0x0701
    PZ_GET_OUTPUTLUT = 0x0702
    PZ_SET_OUTPUTLUTPARAMS = 0x0703
    PZ_REQ_OUTPUTLUTPARAMS = 0x0704
    PZ_GET_OUTPUTLUTPARAMS = 0x0705
    PZ_START_LUTOUTPUT = 0x0706
    PZ_STOP_LUTOUTPUT = 0x0707
    PZ_SET_EEPROMPARAMS = 0x07D0
    PZ_SET_TPZ_DISPSETTINGS = 0x07D1
    PZ_REQ_TPZ_DISPSETTINGS = 0x07D2
    PZ_GET_TPZ_DISPSETTINGS = 0x07D3
    PZ_SET_TPZ_IOSETTINGS = 0x07D4
    PZ_REQ_TPZ_IOSETTINGS = 0x07D5
    PZ_GET_TPZ_IOSETTINGS = 0x07D6
    PZ_SET_ZERO = 0x0658
    PZ_REQ_MAXTRAVEL = 0x0650
    PZ_GET_MAXTRAVEL = 0x0651
    PZ_SET_IOSETTINGS = 0x0670
    PZ_REQ_IOSETTINGS = 0x0671
    PZ_GET_IOSETTINGS = 0x06723
    PZ_SET_OUTPUTMAXVOLTS = 0x0680
    PZ_REQ_OUTPUTMAXVOLTS = 0x0681
    PZ_GET_OUTPUTMAXVOLTS = 0x0682
    PZ_SET_TPZ_SLEWRATES = 0x0683
    PZ_REQ_TPZ_SLEWRATES = 0x0684
    PZ_GET_TPZ_SLEWRATES = 0x068
    MOT_SET_PZSTAGEPARAMDEFAULTS = 0x0686
    PZ_SET_LUTVALUETYPE = 0x0708
    PZ_SET_TSG_IOSETTINGS = 0x07DA
    PZ_REQ_TSG_IOSETTINGS = 0x07DB
    PZ_GET_TSG_IOSETTINGS = 0x07DC
    PZ_REQ_TSG_READING = 0x07DD
    PZ_GET_TSG_READING = 0x07DE

    # NanoTrak Control Messages
    PZ_SET_NTMODE = 0x0603
    PZ_REQ_NTMODE = 0x0604
    PZ_GET_NTMODE = 0x0605
    PZ_SET_NTTRACKTHRESHOLD = 0x0606
    PZ_REQ_NTTRACKTHRESHOLD = 0x0607
    PZ_GET_NTTRACKTHRESHOLD = 0x0608
    PZ_SET_NTCIRCHOMEPOS = 0x0609
    PZ_REQ_NTCIRCHOMEPOS = 0x0610
    PZ_GET_NTCIRCHOMEPOS = 0x0611
    PZ_MOVE_NTCIRCTOHOMEPOS = 0x0612
    PZ_REQ_NTCIRCCENTREPOS = 0x0613
    PZ_GET_NTCIRCCENTREPOS = 0x0614
    PZ_SET_NTCIRCPARAMS = 0x0618
    PZ_REQ_NTCIRCPARAMS = 0x0619
    PZ_GET_NTCIRCPARAMS = 0x0620
    PZ_SET_NTCIRCDIA = 0x061A
    PZ_SET_NTCIRCDIALUT = 0x0621
    PZ_REQ_NTCIRCDIALUT = 0x0622
    PZ_GET_NTCIRCDIALUT = 0x0623
    PZ_SET_NTPHASECOMPPARAMS = 0x0626
    PZ_REQ_NTPHASECOMPPARAMS = 0x0627
    PZ_GET_NTPHASECOMPPARAMS = 0x0628
    PZ_SET_NTTIARANGEPARAMS = 0x0630
    PZ_REQ_NTTIARANGEPARAMS = 0x0631
    PZ_GET_NTTIARANGEPARAMS = 0x0632
    PZ_SET_NTGAINPARAMS = 0x0633
    PZ_REQ_NTGAINPARAMS = 0x0634
    PZ_GET_NTGAINPARAMS = 0x0635
    PZ_SET_NTTIALPFILTERPARAMS = 0x0636
    PZ_REQ_NTTIALPFILTERPARAMS = 0x0637
    PZ_GET_NTTIALPFILTERPARAMS = 0x0638
    PZ_REQ_NTTIAREADING = 0x0639
    PZ_GET_NTTIAREADING = 0x063A
    PZ_SET_NTFEEDBACKSRC = 0x063B
    PZ_REQ_NTFEEDBACKSRC = 0x063C
    PZ_GET_NTFEEDBACKSRC = 0x063D
    PZ_REQ_NTSTATUSBITS = 0x063E
    PZ_GET_NTSTATUSBITS = 0x063F
    PZ_REQ_NTSTATUSUPDATE = 0x0664
    PZ_GET_NTSTATUSUPDATE = 0x0665
    PZ_ACK_NTSTATUSUPDATE = 0x0666
    NT_SET_EEPROMPARAMS = 0x07E7
    NT_SET_TNA_DISPSETTINGS = 0x07E8
    NT_REQ_TNA_DISPSETTINGS = 0x07E9
    NT_GET_TNA_DISPSETTINGS = 0x07EA
    NT_SET_TNAIOSETTINGS = 0x07EB
    NT_REQ_TNAIOSETTINGS = 0x07EC
    NT_GET_TNAIOSETTINGS = 0x07ED

    # Laser Control Messages  181
    LA_SET_PARAMS = 0x0800
    LA_REQ_PARAMS = 0x0801
    LA_GET_PARAMS = 0x0802
    LA_ENABLEOUTPUT = 0x0811
    LA_DISABLEOUTPUT = 0x0812
    LA_REQ_STATUSUPDATE = 0x0820
    LA_GET_STATUSUPDATE = 0x0821
    LA_ACK_STATUSUPDATE = 0x0822

    # Additional messages for TIM101 and KIM101
    PZMOT_SET_PARAMS = 0x08C0
    PZMOT_REQ_PARAMS = 0x08C1
    PZMOT_GET_PARAMS = 0x08C2
    PZMOT_MOVE_ABSOLUTE = 0x08D4
    PZMOT_MOVE_COMPLETED = 0x08D6
    PZMOT_MOVE_JOG = 0x08D9
    PZMOT_GET_STATUSUPDATE = 0x08E1
