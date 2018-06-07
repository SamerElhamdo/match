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
    
        setInterval(function () {
        var SIDE = $(".side-content .active");
        if (SIDE.is(":last-child")) {
                SIDE.fadeOut(function () {
                    $(".side-content div").eq(0).fadeIn().addClass("active").siblings().removeClass("active");
                });
                
        }
                
        SIDE.fadeOut(function () {
            $(this).removeClass("active").next().fadeIn().addClass("active");
        });
    },8000);
    
    
    
        setInterval(function () {
        var SIDE = $(".toggle-button .active");
        if (SIDE.is(":last-child")) {
                $(".toggle-button div").eq(0).addClass("active").siblings().removeClass("active");
        }
                
        SIDE.removeClass("active").next().addClass("active");
    },8000);
    
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
    
});