package com.test.test;

import org.springframework.data.jpa.repository.JpaRepository;

public interface ParitelerRepository extends JpaRepository<Pariteler, Long> {
    // Özel sorguları buraya ekleyebilirsiniz (gerektiği durumda)
}
