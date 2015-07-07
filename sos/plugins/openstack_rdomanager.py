# Copyright (C) 2015 Red Hat, Inc., Lee Yarwood <lyarwood@redhat.com>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

from sos.plugins import Plugin, RedHatPlugin


class OpenStackRDOManager(Plugin):
    """OpenStack RDOManager
    """
    plugin_name = "openstack_rdomanager"
    profiles = ('openstack',)

    def setup(self):
        self.add_copy_spec("/home/stack/.instack/install-undercloud.log")

    def postproc(self):
        protected_log_keys = [
            "UNDERCLOUD_TUSKAR_PASSWORD",
            "UNDERCLOUD_ADMIN_PASSWORD",
            "UNDERCLOUD_CEILOMETER_METERING_SECRET",
            "UNDERCLOUD_CEILOMETER_PASSWORD",
            "UNDERCLOUD_CEILOMETER_SNMPD_PASSWORD",
            "UNDERCLOUD_DB_PASSWORD",
            "UNDERCLOUD_GLANCE_PASSWORD",
            "UNDERCLOUD_HEAT_PASSWORD",
            "UNDERCLOUD_HEAT_STACK_DOMAIN_ADMIN_PASSWORD",
            "UNDERCLOUD_HORIZON_SECRET_KEY",
            "UNDERCLOUD_IRONIC_PASSWORD",
            "UNDERCLOUD_NEUTRON_PASSWORD",
            "UNDERCLOUD_NOVA_PASSWORD",
            "UNDERCLOUD_RABBIT_PASSWORD",
            "UNDERCLOUD_SWIFT_PASSWORD",
            "UNDERCLOUD_TUSKAR_PASSWORD",
            "OS_PASSWORD"
        ]
        regexp = r"((?m)(%s)=)(.*)" % "|".join(protected_log_keys)
        self.do_file_sub("/home/stack/..instack/install-undercloud.log",
                         regexp, r"\1*********")


class RedHatOpenStackRDOManager(OpenStackRDOManager, RedHatPlugin):

    packages = ('python-rdomanager-oscplugin')

    def setup(self):
        super(RedHatOpenStackRDOManager, self).setup()

# vim: set et ts=4 sw=4 :