import rsb
from rst.kinematics.JointAngles_pb2 import JointAngles
from rsb.converter import ProtocolBufferConverter

def main():
	converter = ProtocolBufferConverter(messageClass=JointAngles)
	rsb.converter.registerGlobalConverter(converter)

	rsb.setDefaultParticipantConfig(rsb.ParticipantConfig.fromDefaultSources())

	# print("Registered converter %s" % converter)
	# print("Registered converters:\n%s "
	#      % rsb.converter.getGlobalConverterMap(bytearray))

	with rsb.createInformer("/my/input", dataType=JointAngles) as informer:
		# Send and event using a method that directly accepts data.
		message = JointAngles()
		message.angles.extend([0.707]*29)

		informer.publishData(message)

		print "Message sent: " + str(message)

