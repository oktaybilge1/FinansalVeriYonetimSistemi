package com.test.test;

import org.springframework.data.jpa.repository.JpaRepository;

public interface AltinRepository extends JpaRepository<Altin, Long> {
    // Özel sorguları buraya ekleyebilirsiniz (gerektiği durumda)
}
