    
  $(document).ready(function(){
    $(".icon1 div").click(function(){
        
        
        $(".icon2 div").show();
       $(".icon1 div").hide();
       $(".packer, .foot_packer").fadeOut("slow");
       $(".list_box").toggle("slow");
      //  $(".head_side").css("padding-top", "200px");
      
   })
      });
 
 
       
  $(document).ready(function(){
    
    $(".icon2 div").click(function(){
       
        $(".icon1 div").show();
       $(".icon2 div").hide();
       $(".packer, .foot_packer").fadeIn("slow");
       $(".list_box").toggle("slow");
      //  $(".head_side").css("padding-top", "0");
     
   })
      });
 
 
      
 $(document).ready(function(){
   $(window).scroll(function(){
       var scroll = $(window).scrollTop();
       if (scroll > 100) {
         $(".header").css("background" , "black");
       $(".header").css("box-shadow", "3px 3px 3px 5px rgba(78, 77, 77, 0.774)");
   


       $(document).ready(function(){
        $(".in2").click(function(){
            $(".in1 p").hide();
            $(".in1").css("background-color", "grey");
           
            $(".in2").css('background-color','#333333')
            $(".in2 p").show();
            $(".packer").css('background-color','white')
            $(".small").css('color','black')
            $(".subtitle").css('color','#333333')
            $("i").css('color','lawngreen')
            $(".post_block a button").css('background-color','lawngreen')
            $(".post_details h5").css('color','black')
            $(".post_details p").css('color','black')
            $(".comment_zone h2").css('color','black')
            $(".thread_block").css('color','black')
            $(".thread_block a button i").css('color','white')
            $(".thread_block a button").css('background-color','lawngreen')
            $(".thread_heading h3").css('color','black')
            $(".user h3").css('color','black', 'text-shadow', 'lawngreen')
            $(".user h3").css('text-shadow', '1px 1px lawngreen')
            
         
       })
         
    });
    
    // $(document).ready(function(){
    //     $(".in2").click(function(){
    //         $(".in2").hide();
           
    //         $(".in1").show();
            
    //         $(".images2").fadeOut();
    //         $(".images").fadeIn();
         
    //    })
         
    // });


    
    $(document).ready(function(){
      $(".in1").click(function(){
          $(".in2 p").hide();
          $(".in2").css("background-color", "grey");
         
          $(".in1").css('background-color','#333333')
          $(".in1 p").show();
          $(".packer").css('background-color','black')
          $(".small").css('color','white')
          $(".subtitle").css('color','white')
          $(".post_block a button").css('background-color','rgba(126, 252, 0, 0.637)')
         
          $(".post_details h5").css('color','white')
          $(".post_details p").css('color','white')
          $(".comment_zone h2").css('color','white', 'font-size',"30px")
          $(".thread_block").css('color','white')
          $(".thread_block a button i").css('color','white')
          $(".thread_block a button").css('background-color','rgba(126, 252, 0, 0.637)')
          $(".thread_heading h3").css('color','white')
          $(".user h3").css('color','lawngreen')
            $(".user h3").css('text-shadow', '1px 1px red')
          
       
     })
       
  });








       }
 
       else{
           $(".header").css("background" , "black"); 
       $(".header").css("box-shadow", 'none');	
       }
   })
 })















 ///








