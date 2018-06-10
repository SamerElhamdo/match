$(document).ready(function(){
    //soical media-----------------------------

    var  theDay = $(".day");
    function anmaTe (d) {
        var cards = d.find(".card-match");
        cards.addClass("animate");     
    }
    
    anmaTe(theDay);
    
    (function selctDay () {
        var buttonDay = $(".select-day").find("li");
        buttonDay.click(function () {
            var selct = $(this).attr("name");
            console.log(selct);
            if ($(this).hasClass("active")) {
                console.log("hass class");
            } else {
                $(this).addClass("active").siblings().removeClass("active");
                $(".day.active").fadeOut(100);
                $("div[id=" + selct +"]").fadeIn(400).addClass("active").siblings().removeClass("active");
            }        
        });
    } () );
    
    
    
    
    
    
    
    
    // -------------------------------------------------حركة الايقونات
   
    setInterval(function () {
        var icon = $(".soical-media i.active");
        if (icon.is(":last-child")) {
                $(".soical-media i").eq(0).addClass("active").siblings().removeClass("active");
        }
                
        icon.removeClass("active").next().addClass("active");
    },2000);
    // -------------------------------------------------حركة الايقونات

    
    
    
    
    
    
    
    
    
    
    // -------------------------------------------------الاختيار بين الدوريات و الملخصات
    
/*    var sideD = setInterval(function () {


        var SIDE = $(".side-content .active");
        if (SIDE.is(":last-child")) {
                SIDE.fadeOut(function () {
                    $(".side-content div").eq(0).fadeIn().addClass("active").siblings().removeClass("active");
                });

        }

        SIDE.fadeOut(function () {
            $(this).removeClass("active").next().fadeIn().addClass("active");
        });

        if (x=0){
            clearInterval(samer1);
        }


    },8000);





    var sideU = setInterval(function () {

        var SIDE = $(".toggle-button .active");
        if (SIDE.is(":last-child")) {
                $(".toggle-button div").eq(0).addClass("active").siblings().removeClass("active");
        }

        SIDE.removeClass("active").next().addClass("active");
    },8000);
    
    $(".side-bar").hover(function () {
        clearInterval(sideD);
        clearInterval(sideU);
    });*/
    
    
    (function () {
        $(".toggle-button div").click(function () {
            var selected = $(this).attr("name");
            if ($(this).hasClass("active")) {
                console.log("i hass class");
            } else {
                $(this).addClass("active").siblings().removeClass("active");
                $("div[id=" + selected +"]").addClass("active").siblings().removeClass();
            }
        });
        
    } ());
    
    
    
    
    
    
    
    
    // -------------------------------------------------الاختيار بين الدوريات و الملخصات
    
    
    
    
    
    
    
    
    // change color 
    (function changeColor() {
        var toggleColor = $("#change-color"),
            buttonActive = $("#buttonActive");
            
        $("#tow-color").click(function () {
            
            if (buttonActive.hasClass('active')) {
                buttonActive.toggleClass('active');
                toggleColor.attr("href", "../../../static/css/none");
            } else {
                buttonActive.toggleClass('active');
                toggleColor.attr("href", "/static/css/change-color.css");
            }
            
        });
        
    }());
    
    
    //-----------------------------امنع الافتراضي -------------------------------------------------------------------------------------------
    
    (function () {
        $(".noneHover").click(function (event) {
            var text = $(this).text(),
                defultText = "تبدأ قريباً";
            if (text == defultText) {
                event.preventDefault();
                alert("لم يبدأ البث بعد");
            }
        });
    } ());
    
    
    
    
    
    
    
    
        //-----------------------------امنع الافتراضي -------------------------------------------------------------------------------------------

    
    //change links ----------------------------------------------------------------------------------------------------------------------
    
    (function selcetLink () {
        $("#view").html($("#link-one").text());
        $(".select-link ul li").click(function() {
            var selected = $(this).attr("name");
            $(this).addClass("active").siblings().removeClass("active");
            $("#view").html($("div[id=" + selected +"]").text()); 

        });
        
        
    } ());
    
    //change links ----------------------------------------------------------------------------------------------------------------------

    window.onload= function() {
        Particles.init({
            selector:'.background',
            color: '#ffffff',
            
        });
    };
    
    
});