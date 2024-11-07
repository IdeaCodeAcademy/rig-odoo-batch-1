import { registry } from "@web/core/registry";

import { Component } from  "@odoo/owl";

class MyClientAction extends Component {}
MyClientAction.template = "ica_elearning.clientaction";

// remember the tag name we put in the first step
registry.category("actions").add("ica_elearning.MyClientAction", MyClientAction);