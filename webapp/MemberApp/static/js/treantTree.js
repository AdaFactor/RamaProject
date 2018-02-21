
    var chart_config = {
        chart: {
            container: "#collapsable-example",
            node: {
                HTMLclass: 'node1'
            },
            connectors: {
                type: "curve",
                style: {
                    "stroke-width": 2,
                    "stroke-linecap": "round",
                    "stroke": "#fff"
                }
            }
        },
        nodeStructure: {
            text: {
                name: "name"
            },
            link: {
                href: "http://www.google.com"
            },
            image: "https://png.icons8.com/office/100/000000/user-female-skin-type-4.png",
            children: [
                {
                    text: {
                        name: "name"
                    },
                    link: {
                        href: "http://www.google.com"
                    },                   
                    image: "https://png.icons8.com/office/100/000000/user-female-skin-type-4.png",
                    children: [
                        {
                            text: {
                                name: "name"
                            },
                            link: {
                                href: "http://www.google.com"
                            },
                            image: "https://png.icons8.com/office/100/000000/user-female-skin-type-4.png"
                        }
                    ]
                },
                {
                    text: {
                        name: "name"
                    },
                    link: {
                        href: "http://www.google.com"
                    },
                    image: "https://png.icons8.com/office/100/000000/user-female-skin-type-4.png",
                    children: [
                        {
                            text: {
                                name: "name"
                            },
                            link: {
                                href: "http://www.google.com"
                            },
                            image: "https://png.icons8.com/office/100/000000/user-female-skin-type-4.png"
                        },
                        {
                            text: {
                                name: "name"
                            },
                            link: {
                                href: "http://www.google.com"
                            },
                            image: "https://png.icons8.com/office/100/000000/user-female-skin-type-4.png"
                        }
                    ]
                },
                {
                    text: {
                        name: "name"
                    },
                    link: {
                        href: "http://www.google.com"
                    },
                    image: "https://png.icons8.com/office/100/000000/user-female-skin-type-4.png"
                },
                {
                    text: {
                        name: "name"
                    },
                    link: {
                        href: "http://www.google.com"
                    },
                    image: "https://png.icons8.com/office/100/000000/user-female-skin-type-4.png"
                }
                 
            ]
        }
    };

/* Array approach
    var config = {
        container: "#collapsable-example",
    },
    malory = {
        image: "img/malory.png"
    },

    lana = {
        parent: malory,
        image: "img/lana.png"
    }

    figgs = {
        parent: lana,
        image: "img/figgs.png"
    }

    sterling = {
        parent: malory,
        childrenDropLevel: 1,
        image: "img/sterling.png"
    },

    woodhouse = {
        parent: sterling,
        image: "img/woodhouse.png"
    },

    pseudo = {
        parent: malory,
        pseudo: true
    },

    cheryl = {
        parent: pseudo,
        image: "img/cheryl.png"
    },

    pam = {
        parent: pseudo,
        image: "img/pam.png"
    },

    chart_config = [config, malory, lana, figgs, sterling, woodhouse, pseudo, pam, cheryl];

*/