package com.test.test;

import org.springframework.data.jpa.repository.JpaRepository;

public interface DovizlerRepository extends JpaRepository<Dovizler, Long> {
    // Özel sorguları buraya ekleyebilirsiniz (gerektiği durumda)
}

