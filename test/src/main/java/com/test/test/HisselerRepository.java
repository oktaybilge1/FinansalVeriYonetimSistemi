package com.test.test;

import org.springframework.data.jpa.repository.JpaRepository;

public interface HisselerRepository extends JpaRepository<Hisseler, Long> {
    // Özel sorguları buraya ekleyebilirsiniz (gerektiği durumda)
}
