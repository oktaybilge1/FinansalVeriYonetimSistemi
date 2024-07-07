package com.test.test;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class KriptoParaService {
    private final KriptoParaRepository kriptoParaRepository;
    
    @Autowired
    public KriptoParaService(KriptoParaRepository kriptoParaRepository) {
        this.kriptoParaRepository = kriptoParaRepository;
    }
    
    public List<KriptoPara> getAllKriptoPara() {
        return kriptoParaRepository.findAll();
    }
}
