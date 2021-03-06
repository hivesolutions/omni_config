#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Omni ERP
# Copyright (c) 2008-2020 Hive Solutions Lda.
#
# This file is part of Hive Omni ERP.
#
# Hive Omni ERP is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Omni ERP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Omni ERP. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2020 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

configuration = {
    "default_end_points" : [
        (
            "normal", "", 80, {}
        ),
        (
            "ssl", "", 443, {
                "key_file_path" : "%configuration:pt.hive.colony.plugins.service.http%/frontdoorhq.com.key",
                "certificate_file_path" : "%configuration:pt.hive.colony.plugins.service.http%/frontdoorhq.com.cer"
            }
        )
    ],
    "default_handler" : "file",
    "default_encoding" : None,
    "default_content_type_charset" : "utf-8",
    "default_service_type" : "async",
    "default_client_connection_timeout" : 3,
    "default_connection_timeout" : 30,
    "default_request_timeout" : 3,
    "default_response_timeout" : 30,
    "default_number_threads" : 1,
    "default_scheduling_algorithm" : 2,
    "default_maximum_number_threads" : 30,
    "default_maximum_number_work_threads" : 150,
    "default_work_scheduling_algorithm" : 3,
    "preferred_error_handlers" : [
        "omni",
        "template",
        "default"
    ],
    "verify_request" : False,
    "log_file_path" : "%configuration:pt.hive.colony.plugins.service.http%/access.log",
    "contexts" : {
        "resolution_order" : [
            "/omni_web_error",
            "/"
        ],
        "/omni_web_error" : {
            "handler" : "file",
            "allow_redirection" : False,
            "request_properties" : {
                "base_path" : "$plugin{pt.hive.omni.plugins.web_error}/omni_web_error/resources"
            }
        },
        "/" : {
            "handler" : "file",
            "allow_redirection" : False,
            "request_properties" : {
                "base_path" : "$plugin{pt.hive.omni.plugins.web_error}/omni_web_error/resources",
                "default_page" : "http_service_down.html.tpl"
            }
        }
    }
}
