package com.test.test;

import org.springframework.boot.web.servlet.error.ErrorController;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class CustomErrorController implements ErrorController {

    @RequestMapping("/error")
    public String handleError() {
        // Burada istediğiniz hata sayfasını döndürebilirsiniz
        return "error"; // Örneğin, "error.html" gibi bir sayfa adı
    }
}
