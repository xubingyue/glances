# -*- coding: utf-8 -*-
#
# This file is part of Glances.
#
# Copyright (C) 2014 Nicolargo <nicolas@nicolargo.com>
#
# Glances is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Glances is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# Import Glances libs
from glances.core.glances_stats import GlancesStats
from glances.outputs.glances_curses import glancesCurses


class GlancesStandalone():
    """
    This class creates and manages the Glances standalone session
    """

    def __init__(self, config=None, args=None):

        # Init stats
        self.stats = GlancesStats(config)

        # Initial system informations update
        self.stats.update()

        # Init HTML output
        # !!! TODO
        # if html_tag:
        #     htmloutput = glancesHtml(html_path=output_folder,
        #                              refresh_time=refresh_time)

        # Init CSV output
        # !!! TODO
        # if csv_tag:
        #     csvoutput = glancesCsv(cvsfile=output_file,
        #                            refresh_time=refresh_time)

        # Init screen
        self.screen = glancesCurses(args=args)

    def serve_forever(self):
        """
        Main loop for the CLI
        """
        while True:
            # Update system informations
            self.stats.update()

            # Update the screen
            self.screen.update(self.stats)

            # Update the HTML output
            # !!! TODO
            # if html_tag:
            #     htmloutput.update(stats)

            # Update the CSV output
            # !!! TODO
            # if csv_tag:
            #     csvoutput.update(stats)

    def end(self):
        """
        End of the CLI
        """
        self.screen.end()