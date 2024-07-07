package com.test.test;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.List;


@CrossOrigin(origins = "*")
@RestController
@RequestMapping("/api")
public class ParitelerController {

    @Autowired
    private ParitelerRepository paritelerRepository;

    @GetMapping("/pariteler")
    public List<Pariteler> getPariteler() {
        return paritelerRepository.findAll();
    }
}
