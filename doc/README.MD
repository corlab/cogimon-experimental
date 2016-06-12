source /vol/toolkit/cogimon-minimal-nightly/bin/setup-cogimon-env.sh

deployer-gnulinux

loadService("this","scripting")

scripting.runScript("/vol/toolkit/cogimon-minimal-nightly/etc/cogimon-scenarios/scenario-coman/coman_bring_up_kinchains.ops")

gzclient

rsb0.14 server

rsb0.14 logger socket:/

rsb0.14 send -I/vol/toolkit/cogimon-minimal-nightly/share/rst0.14/proto/stable/ --on-demand-idl-loading=blocking 'pb:.rst.kinematics.JointAngles:{angles: [-0.2,0.5,0,0,0,0,0] }' 'socket:/coman/left_arm/JointPositionCtrl'

Notes:
* var rstrt.kinematics.JointAngles command4 = rstrt.kinematics.JointAngles(7)
