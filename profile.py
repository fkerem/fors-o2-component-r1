#!/usr/bin/env python3
"""POWDER repository profile: one bare d430 and no application startup."""
import geni.portal as portal
import geni.rspec.igext as ig
import geni.rspec.emulab  # Register the Emulab extensions.

pc = portal.Context()
request = pc.makeRequestRSpec()
node = request.RawPC("o2")
node.component_manager_id = "urn:publicid:IDN+emulab.net+authority+cm"
node.hardware_type = "d430"
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD"

tour = ig.Tour()
tour.Description(ig.Tour.MARKDOWN, """
O2 component validation preparation: one d430 running Ubuntu 22.04.
No application startup, radio, spectrum, experiment link or shared VLAN.
POWDER checks out this profile repository; the profile starts no application.
""")
tour.Instructions(ig.Tour.MARKDOWN, """
Wait for the allocated node to be ready and the portal repository checkout
service to show Finished. Check that the selected profile revision matches
the intended profile-r1 tag and commit. Return the experiment status URL,
UUID, node SSH hostname and current displayed expiration to the operator.
No O2 application or test starts automatically. No radio or spectrum is requested.
""")
request.addTour(tour)
pc.printRequestRSpec(request)
