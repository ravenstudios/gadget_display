menu = [
    {
        "title":"SYSTEM",
        "sub_menu":[
            {
                "title":"SHUTDOWN",
                "sub_menu":[
                    {
                        "title":"Yes",
                        "sub_menu":[],
                        "command":["sudo", "shutdown", "-h", "now"],
                        "comment": "Shutting\n Down"
                    },
                    {
                        "title":"No",
                        "sub_menu":[],
                        "command":["No"],
                        "comment": ""
                    },
                ],
                "command":[],
                "comment": ""
            },
            {
                "title":"RESTART",
                "sub_menu":[
                    {
                        "title":"Yes",
                        "sub_menu":[],
                        "command":["sudo", "reboot"],
                        "comment": "Restarting"
                    },
                    {
                        "title":"No",
                        "sub_menu":[],
                        "command":["No"],
                        "comment": ""
                    },
                ],
                "command":[],
                "comment": ""
            },
            {
                "title":"GET IP",
                "sub_menu":[],
                "command":["ip", "a" " | ", "grep", "wlan0"],
                "comment": "comment"
            },
        ],
        "command":[],
        "comment": "comment"
    },
    {
        "title":"MENU 2",
        "sub_menu":[],
        "command":[],
        "comment": "comment"
    },
    {
        "title":"MENU 3",
        "sub_menu":[],
        "command":[],
        "comment": "comment"
    },
]
