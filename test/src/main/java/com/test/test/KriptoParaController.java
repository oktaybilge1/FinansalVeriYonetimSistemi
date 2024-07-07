package com.test.test;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import org.springframework.web.bind.annotation.CrossOrigin;


@CrossOrigin(origins = "*")
@RestController
@RequestMapping("/api")
public class KriptoParaController {
    private final KriptoParaService kriptoParaService;
    
    @Autowired
    public KriptoParaController(KriptoParaService kriptoParaService) {
        this.kriptoParaService = kriptoParaService;
    }
    
    @GetMapping("/kripto-para")
    public List<KriptoPara> getAllKriptoPara() {
        return kriptoParaService.getAllKriptoPara();
    }
}
