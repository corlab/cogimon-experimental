import rsb
from rst.kinematics.JointAngles_pb2 import JointAngles
from rsb.converter import ProtocolBufferConverter

converter = ProtocolBufferConverter(messageClass=JointAngles)
rsb.converter.registerGlobalConverter(converter)

rsb.setDefaultParticipantConfig(rsb.ParticipantConfig.fromDefaultSources())

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class JointInfo():
    def __init__(self, name, initial, min_pos, max_pos):
        self.name = name
        self.initial = initial
        self.max = max_pos
        self.min = min_pos


class MainWindow(Gtk.Window):
    # any signal from the scales is signaled to the label the text of which is
    # changed
    def scale_moved(self, event, scale, name):
        print("Horizontal scale is " + name + " " + str(float(scale.get_value())));
        # if name == 'WaistLat':
        #     print "Setting " + name
        #     self.commanded[0] = scale.get_value()
        # elif name == 'WaistSag':
        #     print "Setting " + name
        #     self.commanded[1] = scale.get_value()
        # elif name == 'WaistYaw':
        #     print "Setting " + name
        #     self.commanded[2] = scale.get_value()
        if name == 'LShSag':
            print "Setting " + name
            self.commanded[0] = scale.get_value()
        elif name == 'LShLat':
            print "Setting " + name
            self.commanded[1] = scale.get_value()
        elif name == 'LShYaw':
            print "Setting " + name
            self.commanded[2] = scale.get_value()
        elif name == 'LElbj':
            print "Setting " + name
            self.commanded[3] = scale.get_value()
        elif name == 'LForearmPlate':
            print "Setting " + name
            self.commanded[4] = scale.get_value()
        elif name == 'LWrj1':
            print "Setting " + name
            self.commanded[5] = scale.get_value()
        elif name == 'LWrj2':
            print "Setting " + name
            self.commanded[6] = scale.get_value()



    def button_clicked(self,button):
        print("Button has been clicked!")
        # Send and event using a method that directly accepts data.
        message = JointAngles()
        message.angles.extend(self.commanded)

        self.informer.publishData(message)

        print "Message sent: " + str(message)

    def __init__(self):
        Gtk.Window.__init__(self, title="Robot GUI Quick Hack")
        self.set_border_width(3)

        self.informer = rsb.createInformer("/coman/left_arm/JointPositionCtrl", dataType=JointAngles)

        # TODO get home / safe posture
        self.commanded = [0] * 7;

        pane = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        pane.set_border_width(10)

        self.notebook = Gtk.Notebook()
        pane.add(self.notebook)

        button = Gtk.Button(label="Apply")
        button.connect("clicked", self.button_clicked)
        pane.add(button)

        self.add(pane)

        robot = {}

        robot['Torso'] = {}
        robot['Torso']['WaistLat'] = JointInfo(0, 0, -1.57, 1.57)
        robot['Torso']['WaistSag'] = JointInfo(0, 0, -1.57, 1.57)
        robot['Torso']['WaistYaw'] = JointInfo(0, 0, -1.57, 1.57)

        # LArm
        robot['Left Arm'] = {}
        robot['Left Arm']['LShSag'] = JointInfo(0, 0, -3.40, 1.65)
        robot['Left Arm']['LShLat'] = JointInfo(0, 0, -0.3, 2)
        robot['Left Arm']['LShYaw'] = JointInfo(0, 0, -1.57, 1.57)
        robot['Left Arm']['LElbj'] = JointInfo(0, 0, -2.3, 0)
        robot['Left Arm']['LForearmPlate'] = JointInfo(0, 0, -1.57, 1.57)
        robot['Left Arm']['LWrj1'] = JointInfo(0, 0, -0.5, 0.5)
        robot['Left Arm']['LWrj2'] = JointInfo(0, 0, -0.78, 1.39)

        for chain, joints in robot.iteritems():
            page = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            page.set_border_width(10)
            for name, info in joints.iteritems():
                hbox = Gtk.Box(spacing=6)
                label = Gtk.Label(name)
                label.set_size_request(100, 30)
                hbox.add(label)

                # two adjustments (initial value, min value, max value,
                # step increment - press cursor keys to see!,
                # page increment - click around the handle to see!,
                # page size - not used here)
                ad1 = Gtk.Adjustment(info.initial, info.min, info.max, 0.1, 1, 0)

                # an horizontal scale
                h_scale = Gtk.Scale(
                    orientation=Gtk.Orientation.HORIZONTAL, adjustment=ad1)
                # of integers (no digits)
                h_scale.set_digits(1)
                # that can expand horizontally if there is space in the grid (see
                # below)
                h_scale.set_hexpand(True)
                # that is aligned at the top of the space allowed in the grid (see
                # below)
                h_scale.set_valign(Gtk.Align.START)
                h_scale.set_size_request(280, 30)
                # hbox.pack_start(h_scale, False, False, 0)
                hbox.add(h_scale)
                h_scale.connect("value-changed", self.scale_moved, h_scale, name)

                # adjustment = Gtk.Adjustment(0, 0, 100, 1, 10, 0)
                # spinbutton = Gtk.SpinButton()
                # spinbutton.set_adjustment(adjustment)
                # hbox.pack_start(spinbutton, False, False, 0)

                # check_numeric = Gtk.CheckButton("Numeric")
                # check_numeric.connect("toggled", self.on_numeric_toggled)
                # hbox.pack_start(check_numeric, False, False, 0)

                # check_ifvalid = Gtk.CheckButton("If Valid")
                # #check_ifvalid.connect("toggled", self.on_ifvalid_toggled)
                # hbox.pack_start(check_ifvalid, False, False, 0)

                page.add(hbox)

            self.notebook.append_page(page, Gtk.Label(chain))


        # self.h_scale.connect("value-changed", self.scale_moved)
        # self.page2.add(self.h_scale)
        # self.page2.set_border_width(10)
        # self.page2.add(Gtk.Label('A page with an image for a Title.'))
        # self.notebook.append_page(
        #     self.page2,
        #     Gtk.Image.new_from_icon_name(
        #         "help-about",
        #         Gtk.IconSize.MENU
        #     )
        #)

    def getinformer(self):
        return self.informer


def main():
    win = MainWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
    win.getinformer().deactivate()

if __name__ == '__main__':
    main()
